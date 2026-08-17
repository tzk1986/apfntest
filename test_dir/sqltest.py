"""
智能菜谱排餐数据查询与导出工具

用于连接数据库查询智能菜谱生成后的排餐数据，生成对应的Excel报表，
方便比对排餐结果与算法设置是否一致。
"""

import logging
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import pandas as pd
import pymysql

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


# ==================== 配置区域 ====================
@dataclass(frozen=True)
class Config:
    """
    全局配置类

    所有参数对应《排餐参数标准化整理.xlsx》中的标准设置。
    反推验证时，程序会自动将推算值与以下配置值进行比对，输出 通过/不通过 判定。
    """

    # ========== 数据库配置 ==========
    DB_HOST: str = "10.50.11.77"
    DB_USER: str = "root"
    DB_PASSWORD: str = "!@#$%^@2021@epfly"
    DB_NAME: str = "ifood_kitchen"
    DB_PORT: int = 3306

    # ========== 排餐计划ID ==========
    PLAN_ID: int = 25080403

    # ========== 消费配置（对应: 排餐参数标准化 - 3.消费配置） ==========
    STANDARD_WEIGHT: float = 350.0  # 人均消耗菜品重量(g)
    WEIGHT_TOLERANCE: float = 0.02  # 重量浮动比例（0-1之间）
    STANDARD_PRICE: float = 24.0  # 人均消费金额(元)
    PRICE_TOLERANCE: float = 0.04  # 价格浮动比例（0-1之间）

    # ========== 大类配比（对应: 排餐参数标准化 - 4.大类配比） ==========
    # 大类重量比例（大荤:小荤:素菜）= 5:3:2，即 50%:30%:20%
    CATEGORY_WEIGHT_RATIO: dict = None  # 各大类目标重量占比，如 {"大荤": 50, "小荤": 30, "素菜": 20}
    # 每日各大类菜品数量
    CATEGORY_DISH_COUNT: dict = None  # 各大类目标菜品数量，如 {"大荤": 8, "小荤": 7, "素菜": 4}
    # 每日各大类热门菜数量
    CATEGORY_HOT_DISH_COUNT: dict = None  # 各大类目标热门菜数量，如 {"大荤": 2, "小荤": 2, "素菜": 1}
    # 大类比例判定容差（百分比）
    CATEGORY_RATIO_TOLERANCE: float = 5.0  # 实际占比与目标占比的最大允许偏差

    # ========== 制作方式配比（对应: 排餐参数标准化 - 5.制作方式配比） ==========
    # 制作方式最低比例（炒菜机:蒸烤箱:人工）= 8:6:5
    COOK_METHOD_RATIO: dict = None  # 各制作方式目标比例，如 {"炒菜机": 8, "蒸烤箱": 6, "人工": 5}
    COOK_METHOD_RATIO_TOLERANCE: float = 2.0  # 制作方式比例判定容差（简化比例允许偏差）

    # ========== 非热门菜重复限制（对应: 排餐参数标准化 - 6.非热门菜重复次数占比） ==========
    NON_HOT_REPEAT_MAX_RATIO: float = 20.0  # 非热门菜重复次数占比上限(%)

    # ========== 菜品最低重量（对应: 排餐参数标准化 - 7.菜品最低重量） ==========
    MIN_DISH_WEIGHT: float = 50.0  # 单道菜品最低出品重量(g)

    # ========== 菜品不连续间隔天数（对应: 排餐参数标准化 - 9.菜品不连续间隔天数） ==========
    MIN_INTERVAL_DAYS: int = 1  # 同一菜品最低间隔出现天数（0=不限制, 1=至少间隔1天即不可连续）

    # ========== 输出目录 ==========
    OUTPUT_DIR: str = r"d:\tangzk\py\seldom-web-testing\reports"

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

    def __post_init__(self):
        # 设置默认字典值（frozen dataclass 需要用 object.__setattr__）
        if self.CATEGORY_WEIGHT_RATIO is None:
            object.__setattr__(self, "CATEGORY_WEIGHT_RATIO", {"大荤": 50, "小荤": 30, "素菜": 20})
        if self.CATEGORY_DISH_COUNT is None:
            object.__setattr__(self, "CATEGORY_DISH_COUNT", {"大荤": 8, "小荤": 7, "素菜": 4})
        if self.CATEGORY_HOT_DISH_COUNT is None:
            object.__setattr__(self, "CATEGORY_HOT_DISH_COUNT", {"大荤": 2, "小荤": 2, "素菜": 1})
        if self.COOK_METHOD_RATIO is None:
            object.__setattr__(self, "COOK_METHOD_RATIO", {"炒菜机": 8, "蒸烤箱": 6, "人工": 5})

    @property
    def db_config(self) -> dict:
        """获取数据库连接配置"""
        return {
            "host": self.DB_HOST,
            "user": self.DB_USER,
            "password": self.DB_PASSWORD,
            "database": self.DB_NAME,
            "port": self.DB_PORT,
        }


# 全局配置实例
config = Config()


# ==================== 常量定义 ====================
# 星期映射（英文 -> 中文）
DAY_NAME_MAP = {
    "Monday": "星期一",
    "Tuesday": "星期二",
    "Wednesday": "星期三",
    "Thursday": "星期四",
    "Friday": "星期五",
    "Saturday": "星期六",
    "Sunday": "星期日",
}

# 预估用餐人数（按星期）
ESTIMATED_PEOPLE = {
    "星期一": 300,
    "星期二": 280,
    "星期三": 280,
    "星期四": 280,
    "星期五": 250,
}


# ==================== 工具函数 ====================
@contextmanager
def get_db_connection():
    """数据库连接上下文管理器"""
    connection = None
    try:
        connection = pymysql.connect(**config.db_config)
        logger.info("数据库连接成功")
        yield connection
    finally:
        if connection and connection.open:
            connection.close()
            logger.info("数据库连接已关闭")


def get_output_path(filename: str) -> Path:
    """获取输出文件完整路径"""
    output_dir = Path(config.OUTPUT_DIR)
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir / filename


def add_weekday_column(df: pd.DataFrame, date_col: str = "日期") -> pd.DataFrame:
    """添加中文星期列"""
    if date_col not in df.columns:
        logger.warning(f"数据中未找到 '{date_col}' 列，无法添加星期信息")
        return df

    df = df.copy()
    df["星期"] = pd.to_datetime(df[date_col]).dt.day_name().map(DAY_NAME_MAP)
    return df


def add_estimated_people_column(df: pd.DataFrame) -> pd.DataFrame:
    """添加预估人数列"""
    df = df.copy()
    df["预估人数"] = df["星期"].map(ESTIMATED_PEOPLE)
    return df


def build_plan_query(plan_id: Optional[int] = None) -> str:
    """构建带plan_id过滤的SQL条件"""
    plan_id = plan_id or config.PLAN_ID
    return f"m.plan_id = {plan_id}"


# ==================== SQL查询模板 ====================
def get_query1(plan_id: Optional[int] = None) -> str:
    """查询1：每天排餐菜品和重量数据（含小类）"""
    plan_condition = build_plan_query(plan_id)
    return f"""SELECT
        m.cook_date AS 日期,
        d.dish_name AS 菜名,
        m.cook_weight AS 重量,
        d.price AS 50克价格,
        d.category1 AS 大类,
        d.category2 AS 小类,
        d.popular_flag AS 热门菜,
        d.cook_method AS 制作方式
    FROM
        algorithm_test_dish d
        INNER JOIN algorithm_test_plan_item m ON d.id = m.dish_id
    WHERE
        {plan_condition}
    ORDER BY
        m.cook_date;"""


def get_query2(plan_id: Optional[int] = None) -> str:
    """查询2：每天排餐菜品的总重量和总价格"""
    plan_condition = build_plan_query(plan_id)
    return f"""SELECT
        m.cook_date AS 日期,
        SUM(m.cook_weight) AS 总重量,
        SUM((m.cook_weight / 50) * d.price) AS 总价格
    FROM
        algorithm_test_plan_item m
        INNER JOIN algorithm_test_dish d ON m.dish_id = d.id
    WHERE
        {plan_condition}
    GROUP BY
        m.cook_date
    ORDER BY
        日期;"""


def get_query3(plan_id: Optional[int] = None) -> str:
    """查询3：每天大类排餐的总重量"""
    plan_condition = build_plan_query(plan_id)
    return f"""SELECT
        m.cook_date AS 日期,
        d.category1 AS 菜品大类,
        SUM(m.cook_weight) AS 分类总重量
    FROM
        algorithm_test_plan_item m
        INNER JOIN algorithm_test_dish d ON m.dish_id = d.id
    WHERE
        {plan_condition}
    GROUP BY
        m.cook_date, d.category1
    ORDER BY
        日期, 菜品大类;"""


def get_category_query(plan_id: Optional[int] = None) -> str:
    """分类占比查询"""
    plan_condition = build_plan_query(plan_id)
    return f"""SELECT
        m.cook_date AS 日期,
        d.category1 AS 菜品大类,
        SUM(m.cook_weight) AS 分类总重量
    FROM
        algorithm_test_plan_item m
        INNER JOIN algorithm_test_dish d ON m.dish_id = d.id
    WHERE
        {plan_condition}
    GROUP BY
        m.cook_date, d.category1
    ORDER BY
        日期, 菜品大类;"""


def get_detailed_category_query(plan_id: Optional[int] = None) -> str:
    """细化分类查询"""
    plan_condition = build_plan_query(plan_id)
    return f"""SELECT
        m.cook_date AS 日期,
        d.category1 AS 菜品大类,
        d.category2 AS 细化分类,
        COUNT(d.id) AS 分类数量
    FROM
        algorithm_test_plan_item m
        INNER JOIN algorithm_test_dish d ON m.dish_id = d.id
    WHERE
        {plan_condition}
    GROUP BY
        m.cook_date, d.category1, d.category2
    ORDER BY
        日期, 菜品大类, 细化分类;"""


def get_popular_rate_query(plan_id: Optional[int] = None) -> str:
    """热门度与排餐次数查询"""
    plan_condition = build_plan_query(plan_id)
    return f"""SELECT
        d.dish_name AS 菜名,
        d.popular_rate AS 热门度,
        COUNT(m.id) AS 排餐次数
    FROM
        algorithm_test_dish d
        INNER JOIN algorithm_test_plan_item m ON d.id = m.dish_id
    WHERE
        d.popular_rate != 0
        AND {plan_condition}
    GROUP BY
        d.dish_name, d.popular_rate
    ORDER BY
        d.popular_rate DESC, 排餐次数 DESC;"""


# ==================== 数据处理函数 ====================
def calculate_category_summary(df: pd.DataFrame) -> pd.DataFrame:
    """计算分类占比汇总"""
    df = df.copy()
    df["日期"] = pd.to_datetime(df["日期"])

    total_weight = df.groupby("日期")["分类总重量"].transform("sum")
    df["分类占比"] = (df["分类总重量"] / total_weight * 100).round(2)

    summary = df.pivot(index="日期", columns="菜品大类", values="分类占比").fillna(0)
    summary["分类占比汇总"] = summary.apply(
        lambda row: "（大荤:小荤:素菜）："
        + ":".join(f"{row.get(cat, 0):.2f}%" for cat in ["大荤", "小荤", "素菜"]),
        axis=1,
    )
    return summary.reset_index()[["日期", "分类占比汇总"]]


def calculate_cook_method_summary(df: pd.DataFrame) -> pd.DataFrame:
    """计算制作方式比例"""
    df = df.copy()
    summary = df.groupby(["日期", "制作方式"]).size().unstack(fill_value=0)

    summary["制作方式比例"] = summary.apply(
        lambda row: "（炒菜机:蒸烤箱:人工）：" + ":".join(row.astype(str)),
        axis=1,
    )
    return summary.reset_index()[["日期", "制作方式比例"]]


def calculate_hot_dish_summary(df: pd.DataFrame) -> pd.DataFrame:
    """计算热门菜统计"""
    df = df.copy()
    hot_data = df[df["热门菜"] == "是"]

    hot_summary = (
        hot_data.groupby(["日期", "大类"]).size().reset_index(name="热门菜数量")
    )
    hot_summary["热门菜统计"] = hot_summary.apply(
        lambda row: f"{row['大类']}（{int(row['热门菜数量'])}）", axis=1
    )

    result = (
        hot_summary.groupby("日期")["热门菜统计"]
        .apply(lambda x: "，".join(x))
        .reset_index(name="每日热门菜统计")
    )
    return result


def calculate_weight_analysis(df: pd.DataFrame) -> pd.DataFrame:
    """计算重量相关分析指标"""
    df = df.copy()
    standard_weight = config.STANDARD_WEIGHT
    tolerance = config.WEIGHT_TOLERANCE

    low = standard_weight * (1 - tolerance)
    high = standard_weight * (1 + tolerance)

    df["重量浮动范围"] = f"{low:.2f}-{high:.2f}"
    df["重量浮动值"] = (df["人均消耗重量"] - standard_weight).round(2)
    df["重量是否在范围内"] = df["人均消耗重量"].apply(
        lambda x: "在范围内" if low <= x <= high else "超出范围"
    )
    return df


def calculate_price_analysis(df: pd.DataFrame) -> pd.DataFrame:
    """计算价格相关分析指标"""
    df = df.copy()
    standard_price = config.STANDARD_PRICE
    tolerance = config.PRICE_TOLERANCE

    low = standard_price * (1 - tolerance)
    high = standard_price * (1 + tolerance)

    df["价格浮动范围"] = f"{low:.2f}-{high:.2f}"
    df["价格浮动值"] = (df["人均消费金额"] - standard_price).round(2)
    df["价格是否在范围内"] = df["人均消费金额"].apply(
        lambda x: "在范围内" if low <= x <= high else "超出范围"
    )
    return df


def calculate_repetition_rate(df: pd.DataFrame) -> pd.DataFrame:
    """计算菜品重复排餐比例"""
    df = df.copy()
    df["周数"] = df["日期"].dt.isocalendar().week

    weekly_counts = df.groupby(["周数", "菜名"]).size().reset_index(name="排餐次数")
    weekly_counts["重复次数"] = (weekly_counts["排餐次数"] - 1).clip(lower=0)

    total_per_week = weekly_counts.groupby("周数")["排餐次数"].transform("sum")
    weekly_counts["重复比例"] = (weekly_counts["重复次数"] / total_per_week).round(4)

    df = pd.merge(
        df,
        weekly_counts[["周数", "菜名", "重复比例"]],
        on=["周数", "菜名"],
        how="left",
    )
    return df


def check_consecutive_meals(df: pd.DataFrame) -> pd.DataFrame:
    """检查连续排餐标记"""
    df = df.copy()
    df["日期"] = pd.to_datetime(df["日期"])
    df = df.sort_values(by=["菜名", "日期"])
    df["连续排餐标记"] = (
        (df["菜名"] == df["菜名"].shift(1))
        & (df["日期"] - df["日期"].shift(1) == pd.Timedelta(days=1))
    ).astype(int)
    return df


# ==================== 参数反推函数 ====================
def reverse_engineer_parameters(plan_id: Optional[int] = None) -> None:
    """
    从排餐数据中反推算法参数设置，生成参数验证报告

    ================================================================================
    数据来源说明
    ================================================================================
    本函数通过查询数据库中的排餐计划数据，反推出算法的参数设置，
    用于与标准参数文档（排餐参数标准化整理.xlsx）进行比对验证。

    数据来源表:
    - algorithm_test_plan_item: 排餐计划明细表（plan_id, dish_id, cook_date, cook_weight）
    - algorithm_test_dish: 菜品信息表（id, dish_name, category1, category2, price, popular_flag, cook_method）

    ================================================================================
    反推参数及计算公式
    ================================================================================

    1. 排餐天数
       - 数据来源: query1 的日期字段
       - 计算公式: COUNT(DISTINCT cook_date)
       - 对应参数: 排餐参数标准化 - 排餐周期配置 - 天序号

    2. 每日就餐人数
       - 数据来源: 配置文件 ESTIMATED_PEOPLE 按星期映射
       - 计算公式: 根据cook_date计算星期，映射对应人数
       - 对应参数: 排餐参数标准化 - 排餐周期配置 - 就餐人数

    3. 人均消耗菜品重量(g)
       - 数据来源: query2 的总重量 / 预估人数
       - 计算公式: SUM(cook_weight) / 预估人数
       - 浮动比例推算: MAX(|实际值-均值|/均值)
       - 对应参数: 排餐参数标准化 - 消费配置 - 人均重量、重量浮动比例
       - 判定逻辑: 平均值在[STANDARD_WEIGHT*(1±WEIGHT_TOLERANCE)]范围内 且 每天均在范围内

    4. 人均消费金额(元)
       - 数据来源: query2 的总价格 / 预估人数
       - 计算公式: SUM((cook_weight/50) * price) / 预估人数
       - 浮动比例推算: MAX(|实际值-均值|/均值)
       - 对应参数: 排餐参数标准化 - 消费配置 - 人均金额、价格浮动比例
       - 判定逻辑: 平均值在[STANDARD_PRICE*(1±PRICE_TOLERANCE)]范围内 且 每天均在范围内

    5. 大类重量比例
       - 数据来源: category_data 的分类总重量
       - 计算公式: 各大类SUM(cook_weight) / 总重量 * 100
       - 简化比例: 各占比 / 最小占比（取整）
       - 对应参数: 排餐参数标准化 - 大类配比 - 重量比例
       - 判定逻辑: 实际占比与CATEGORY_WEIGHT_RATIO偏差 <= CATEGORY_RATIO_TOLERANCE%

    6. 制作方式比例
       - 数据来源: query1 的制作方式字段
       - 计算公式: 各制作方式每日数量均值，简化比例（除以最小值取整）
       - 对应参数: 排餐参数标准化 - 制作方式配比
       - 判定逻辑: 简化比例与COOK_METHOD_RATIO偏差 <= COOK_METHOD_RATIO_TOLERANCE

    7. 每日菜品数量（按大类）
       - 数据来源: query1 按日期和大类分组计数
       - 计算公式: COUNT(dish_name) GROUP BY 日期, 大类
       - 对应参数: 排餐参数标准化 - 大类配比 - 数量
       - 判定逻辑: 实际数量与CATEGORY_DISH_COUNT偏差 <= 1道

    8. 热门菜数量
       - 数据来源: query1 筛选 popular_flag = "是"
       - 计算公式: COUNT(dish_name) WHERE popular_flag='是' GROUP BY 大类
       - 对应参数: 排餐参数标准化 - 菜品源数据 - 热门菜
       - 判定逻辑: 实际数量与CATEGORY_HOT_DISH_COUNT偏差 <= 1道

    9. 非热门菜重复次数占比
        - 数据来源: query1 筛选 popular_flag != "是"
        - 计算公式: SUM(MAX(0, 排餐次数-1)) / 非热门菜总排餐数 * 100%
        - 对应参数: 排餐参数标准化 - 非热门菜重复次数占比
        - 判定逻辑: 推算占比 <= NON_HOT_REPEAT_MAX_RATIO%

    10. 菜品最低重量
        - 数据来源: query1 的重量字段
        - 计算公式: MIN(cook_weight)
        - 对应参数: 排餐参数标准化 - 菜品最低重量
        - 判定逻辑: 推算值 >= MIN_DISH_WEIGHT

    11. 菜品不连续间隔天数
        - 数据来源: query1 按菜名和日期排序
        - 计算公式: MIN(DATEDIFF(当前日期, 上次日期))，同菜品相邻两次排餐的最小间隔
        - 对应参数: 排餐参数标准化 - 菜品不连续间隔天数
        - 判定逻辑: 推算值 >= MIN_INTERVAL_DAYS

    12. 连续排餐违规检查
        - 计算公式: 同菜品连续两天出现标记为违规
        - 对应规则: 排餐规则 - 规则12 - 连续2天不可出现同一道菜
        - 判定逻辑: MIN_INTERVAL_DAYS >= 1 时，违规数必须为0

    13. 热门菜窗口期分析
        - 数据来源: query1 筛选热门菜
        - 计算公式: COUNT(出现次数) GROUP BY 菜名
        - 对应参数: 排餐参数标准化 - 菜品源数据 - 窗口周期内出现次数

    ================================================================================
    输出文件说明
    ================================================================================
    输出文件: parameter_verification.xlsx

    Sheet1 - 参数反推报告:
        包含所有反推参数及其推算值、配置值、判定结果（通过/不通过）

    Sheet2 - 验证结果汇总:
        所有验证项的判定结果汇总，便于快速查看整体情况

    Sheet3 - 每日汇总数据:
        日期、星期、总重量、总价格、预估人数、人均消耗重量、人均消费金额

    Sheet4 - 大类每日占比:
        每日各大类（大荤/小荤/素菜）的重量占比百分比

    Sheet5 - 推算公式说明:
        详细的推算公式和数据来源说明
    ================================================================================
    """
    plan_id = plan_id or config.PLAN_ID
    output_file = get_output_path("parameter_verification.xlsx")

    try:
        with get_db_connection() as conn:
            # 查询基础数据
            query1_data = pd.read_sql(get_query1(plan_id), conn)
            query1_data["日期"] = pd.to_datetime(query1_data["日期"])

            query2_data = pd.read_sql(get_query2(plan_id), conn)
            query2_data["日期"] = pd.to_datetime(query2_data["日期"])

            # 分类数据
            category_data = pd.read_sql(get_category_query(plan_id), conn)
            category_data["日期"] = pd.to_datetime(category_data["日期"])

        # ========== 1. 排餐天数 ==========
        # 公式: COUNT(DISTINCT cook_date) FROM algorithm_test_plan_item WHERE plan_id = ?
        total_days = query1_data["日期"].nunique()
        dates = sorted(query1_data["日期"].unique())

        # ========== 2. 每日就餐人数 ==========
        # 数据来源: 配置文件 ESTIMATED_PEOPLE
        # 映射规则: 星期一到星期五分别对应 300, 280, 280, 280, 250
        date_info = pd.DataFrame({"日期": dates})
        date_info["星期"] = date_info["日期"].dt.day_name().map(DAY_NAME_MAP)
        date_info["就餐人数"] = date_info["星期"].map(ESTIMATED_PEOPLE)

        # ========== 3. 人均消耗重量分析 ==========
        # 公式: 人均消耗重量 = 总重量 / 预估人数
        # 浮动比例 = MAX(|实际值-均值| / 均值)
        query2_with_weekday = add_weekday_column(query2_data)
        query2_with_weekday["预估人数"] = query2_with_weekday["星期"].map(ESTIMATED_PEOPLE)
        query2_with_weekday["人均消耗重量"] = (
            query2_with_weekday["总重量"] / query2_with_weekday["预估人数"]
        ).round(2)
        query2_with_weekday["人均消费金额"] = (
            query2_with_weekday["总价格"] / query2_with_weekday["预估人数"]
        ).round(2)

        # 计算重量浮动比例
        # 公式: tolerance = MAX(|min-avg|/avg, |max-avg|/avg)
        avg_weight = query2_with_weekday["人均消耗重量"].mean()
        min_weight = query2_with_weekday["人均消耗重量"].min()
        max_weight = query2_with_weekday["人均消耗重量"].max()
        actual_weight_tolerance = max(
            abs(min_weight - avg_weight) / avg_weight,
            abs(max_weight - avg_weight) / avg_weight,
        )

        # ========== 4. 人均消费金额分析 ==========
        # 公式: 人均消费金额 = 总价格 / 预估人数
        # 总价格 = SUM((cook_weight / 50) * price)
        avg_price = query2_with_weekday["人均消费金额"].mean()
        min_price = query2_with_weekday["人均消费金额"].min()
        max_price = query2_with_weekday["人均消费金额"].max()
        actual_price_tolerance = max(
            abs(min_price - avg_price) / avg_price,
            abs(max_price - avg_price) / avg_price,
        )

        # ========== 5. 大类重量比例 ==========
        # 公式: 大类占比 = SUM(分类总重量) / SUM(所有总重量) * 100%
        # 简化比例: 各占比 / 最小占比（四舍五入取整）
        total_weight_by_category = category_data.groupby("菜品大类")["分类总重量"].sum()
        total_weight_all = total_weight_by_category.sum()
        category_ratio = (total_weight_by_category / total_weight_all * 100).round(2)

        min_ratio = category_ratio.min()
        simplified_ratio = (category_ratio / min_ratio).round(0).astype(int)

        # ========== 6. 制作方式统计 ==========
        # 公式: 各制作方式每日数量 = COUNT(dish_name) GROUP BY 日期, 制作方式
        # 简化比例: 各均值 / 最小均值（四舍五入取整）
        cook_method_by_day = query1_data.groupby(["日期", "制作方式"]).size().unstack(fill_value=0)
        avg_cook_method = cook_method_by_day.mean().round(0).astype(int)

        min_method = avg_cook_method[avg_cook_method > 0].min()
        simplified_method_ratio = (avg_cook_method / min_method).round(0).astype(int)

        # ========== 7. 每日菜品分类统计 ==========
        # 公式: 每日各大类菜品数量 = COUNT(dish_name) GROUP BY 日期, 大类
        daily_category_count = query1_data.groupby(["日期", "大类"]).size().unstack(fill_value=0)
        avg_category_count = daily_category_count.mean().round(1)

        # ========== 8. 热门菜统计 ==========
        # 公式: 热门菜数量 = COUNT(dish_name) WHERE popular_flag = '是' GROUP BY 大类
        hot_dish_data = query1_data[query1_data["热门菜"] == "是"]
        hot_dish_by_category = hot_dish_data.groupby(["日期", "大类"]).size().unstack(fill_value=0)
        avg_hot_dish = hot_dish_by_category.mean().round(1)

        # ========== 9. 小类统计 ==========
        # 数据来源: algorithm_test_dish 表的 category2 字段
        # 公式: COUNT(dish_name) GROUP BY 大类, 小类
        dish_detail_query = f"""SELECT
            d.dish_name AS 菜名,
            d.category1 AS 大类,
            d.category2 AS 小类,
            d.popular_flag AS 热门菜
        FROM
            algorithm_test_dish d
            INNER JOIN algorithm_test_plan_item m ON d.id = m.dish_id
        WHERE
            m.plan_id = {plan_id}
        GROUP BY
            d.dish_name, d.category1, d.category2, d.popular_flag
        """
        with get_db_connection() as conn:
            dish_detail = pd.read_sql(dish_detail_query, conn)

        subcategory_stats = dish_detail.groupby(["大类", "小类"])["菜名"].count().reset_index()
        subcategory_stats.columns = ["大类", "小类", "数量"]

        # ========== 10. 非热门菜重复占比 ==========
        # 公式: 重复占比 = SUM(MAX(0, 排餐次数-1)) / 非热门菜总排餐数 * 100%
        # 说明: 每重复1次累计+1，除以总排餐数
        non_hot_data = query1_data[query1_data["热门菜"] != "是"]
        dish_counts = non_hot_data.groupby("菜名").size()
        repeat_counts = (dish_counts - 1).clip(lower=0)
        total_repeat = repeat_counts.sum()
        total_dish_slots = len(non_hot_data)
        repeat_ratio = (total_repeat / total_dish_slots * 100) if total_dish_slots > 0 else 0

        # ========== 11. 菜品最低重量 ==========
        # 公式: MIN(cook_weight) FROM algorithm_test_plan_item WHERE plan_id = ?
        min_dish_weight = query1_data["重量"].min()

        # ========== 12. 连续排餐检查 ==========
        # 公式: 同菜品相邻两次排餐的最小日期差
        # DATEDIFF(当前日期, 上次日期) GROUP BY 菜名
        query1_sorted = query1_data.sort_values(["菜名", "日期"])
        date_diffs = query1_sorted.groupby("菜名")["日期"].diff()
        min_interval = date_diffs.dropna().dt.days.min() if len(date_diffs.dropna()) > 0 else 0

        # ========== 13. 热门菜窗口期分析 ==========
        # 公式: COUNT(日期) WHERE popular_flag = '是' GROUP BY 菜名
        hot_dish_in_plan = query1_data[query1_data["热门菜"] == "是"]
        hot_dish_freq = hot_dish_in_plan.groupby("菜名").size()

        # ========== 构建参数反推报告 ==========
        # report_data: [参数名称, 配置值, 推算值, 判定结果, 说明]
        report_data = []
        formula_data = []  # 推算公式说明
        results = []  # 汇总判定结果: [参数名称, 判定, 说明]

        # 报告标题
        report_data.append(["=" * 80])
        report_data.append(["排餐参数反推验证报告"])
        report_data.append([f"排餐计划ID: {plan_id}"])
        report_data.append(["=" * 80])
        report_data.append([""])

        # 公式说明表头
        formula_data.append(["参数名称", "数据来源", "计算公式", "对应标准参数"])

        # ------------------------------------------------------------------
        # 1. 排餐天数
        # ------------------------------------------------------------------
        report_data.append(["【1. 排餐天数】"])
        report_data.append(["  实际排餐天数", "", total_days, "", ""])
        formula_data.append([
            "排餐天数",
            "algorithm_test_plan_item.cook_date",
            "COUNT(DISTINCT cook_date)",
            "排餐参数标准化 - 排餐周期配置 - 天序号"
        ])
        report_data.append([""])

        # ------------------------------------------------------------------
        # 2. 每日就餐人数
        # ------------------------------------------------------------------
        report_data.append(["【2. 每日就餐人数】"])
        for _, row in date_info.iterrows():
            report_data.append([f"  {row['日期'].strftime('%Y-%m-%d')} ({row['星期']})", "", row["就餐人数"], "", ""])
        formula_data.append([
            "就餐人数",
            "配置常量 ESTIMATED_PEOPLE",
            "根据日期计算星期，映射对应人数",
            "排餐参数标准化 - 排餐周期配置 - 就餐人数"
        ])
        report_data.append([""])

        # ------------------------------------------------------------------
        # 3. 人均消耗菜品重量（已配置: STANDARD_WEIGHT, WEIGHT_TOLERANCE）
        # ------------------------------------------------------------------
        # 判定逻辑:
        #   - 平均值是否在 [STANDARD_WEIGHT*(1-WEIGHT_TOLERANCE), STANDARD_WEIGHT*(1+WEIGHT_TOLERANCE)] 范围内
        #   - 每天的人均值是否都在浮动范围内
        weight_low = config.STANDARD_WEIGHT * (1 - config.WEIGHT_TOLERANCE)
        weight_high = config.STANDARD_WEIGHT * (1 + config.WEIGHT_TOLERANCE)
        weight_avg_pass = weight_low <= avg_weight <= weight_high
        # 统计每天超出浮动范围的天数
        weight_out_of_range_days = (
            (query2_with_weekday["人均消耗重量"] < weight_low)
            | (query2_with_weekday["人均消耗重量"] > weight_high)
        ).sum()
        weight_day_pass = weight_out_of_range_days == 0
        weight_pass = weight_avg_pass and weight_day_pass

        report_data.append(["【3. 人均消耗菜品重量】", "配置值", "推算值", "判定", "说明"])
        report_data.append(["  标准人均重量", f"{config.STANDARD_WEIGHT}g", f"{avg_weight:.2f}g",
                            "通过" if weight_avg_pass else "不通过",
                            f"允许范围: {weight_low:.2f}-{weight_high:.2f}g"])
        report_data.append(["  重量浮动比例", f"{config.WEIGHT_TOLERANCE}", f"{actual_weight_tolerance:.4f}",
                            "通过" if actual_weight_tolerance <= config.WEIGHT_TOLERANCE + 0.005 else "不通过",
                            f"推算值应<=配置值+0.005"])
        report_data.append(["  每日均在范围内", "0天超出", f"{weight_out_of_range_days}天超出",
                            "通过" if weight_day_pass else "不通过",
                            f"共{len(query2_with_weekday)}天排餐"])
        results.append(["人均消耗重量", "通过" if weight_pass else "不通过",
                        f"均值{avg_weight:.1f}g, 浮动{actual_weight_tolerance:.4f}"])
        formula_data.append([
            "人均消耗重量",
            "algorithm_test_plan_item.cook_weight / 预估人数",
            "人均消耗 = SUM(cook_weight) / 预估人数\n浮动比例 = MAX(|实际值-均值|/均值)",
            "排餐参数标准化 - 消费配置 - 人均重量、重量浮动比例"
        ])
        report_data.append([""])

        # ------------------------------------------------------------------
        # 4. 人均消费金额（已配置: STANDARD_PRICE, PRICE_TOLERANCE）
        # ------------------------------------------------------------------
        price_low = config.STANDARD_PRICE * (1 - config.PRICE_TOLERANCE)
        price_high = config.STANDARD_PRICE * (1 + config.PRICE_TOLERANCE)
        price_avg_pass = price_low <= avg_price <= price_high
        price_out_of_range_days = (
            (query2_with_weekday["人均消费金额"] < price_low)
            | (query2_with_weekday["人均消费金额"] > price_high)
        ).sum()
        price_day_pass = price_out_of_range_days == 0
        price_pass = price_avg_pass and price_day_pass

        report_data.append(["【4. 人均消费金额】", "配置值", "推算值", "判定", "说明"])
        report_data.append(["  标准人均金额", f"{config.STANDARD_PRICE}元", f"{avg_price:.2f}元",
                            "通过" if price_avg_pass else "不通过",
                            f"允许范围: {price_low:.2f}-{price_high:.2f}元"])
        report_data.append(["  价格浮动比例", f"{config.PRICE_TOLERANCE}", f"{actual_price_tolerance:.4f}",
                            "通过" if actual_price_tolerance <= config.PRICE_TOLERANCE + 0.005 else "不通过",
                            f"推算值应<=配置值+0.005"])
        report_data.append(["  每日均在范围内", "0天超出", f"{price_out_of_range_days}天超出",
                            "通过" if price_day_pass else "不通过",
                            f"共{len(query2_with_weekday)}天排餐"])
        results.append(["人均消费金额", "通过" if price_pass else "不通过",
                        f"均值{avg_price:.2f}元, 浮动{actual_price_tolerance:.4f}"])
        formula_data.append([
            "人均消费金额",
            "algorithm_test_plan_item.cook_weight * algorithm_test_dish.price / 预估人数",
            "人均金额 = SUM((cook_weight/50) * price) / 预估人数\n浮动比例 = MAX(|实际值-均值|/均值)",
            "排餐参数标准化 - 消费配置 - 人均金额、价格浮动比例"
        ])
        report_data.append([""])

        # ------------------------------------------------------------------
        # 5. 制作方式比例（已配置: COOK_METHOD_RATIO）
        # ------------------------------------------------------------------
        method_str = ":".join([str(v) for v in simplified_method_ratio.values])
        method_detail = ":".join([str(v) for v in avg_cook_method.values])
        config_method_str = ":".join([str(v) for v in config.COOK_METHOD_RATIO.values()])

        # 判定: 简化比例是否与配置比例一致（允许TOLERANCE偏差）
        method_pass = True
        method_details = []
        for method_name in config.COOK_METHOD_RATIO:
            actual_val = simplified_method_ratio.get(method_name, 0)
            config_val = config.COOK_METHOD_RATIO[method_name]
            diff = abs(actual_val - config_val)
            ok = diff <= config.COOK_METHOD_RATIO_TOLERANCE
            if not ok:
                method_pass = False
            method_details.append(f"{method_name}: 配置{config_val}/推算{actual_val}")

        report_data.append(["【5. 制作方式比例】", "配置值", "推算值", "判定", "说明"])
        report_data.append(["  配置比例", config_method_str, method_str,
                            "通过" if method_pass else "不通过",
                            f"容差: ±{config.COOK_METHOD_RATIO_TOLERANCE}"])
        report_data.append(["  日均数量", "", method_detail, "", ""])
        for detail in method_details:
            report_data.append([f"    {detail}"])
        results.append(["制作方式比例", "通过" if method_pass else "不通过",
                        "; ".join(method_details)])
        formula_data.append([
            "制作方式比例",
            "algorithm_test_dish.cook_method",
            "COUNT(dish_name) GROUP BY 日期, 制作方式\n简化比例 = 各均值 / 最小均值",
            "排餐参数标准化 - 制作方式配比"
        ])
        report_data.append([""])

        # ------------------------------------------------------------------
        # 6. 大类重量比例（已配置: CATEGORY_WEIGHT_RATIO）
        # ------------------------------------------------------------------
        ratio_str = ":".join([str(v) for v in simplified_ratio.values])
        ratio_detail = ":".join([f"{v:.1f}%" for v in category_ratio.values])
        config_ratio_str = ":".join([f"{v}%" for v in config.CATEGORY_WEIGHT_RATIO.values()])

        # 判定: 实际占比与配置占比的偏差是否在容差范围内
        category_pass = True
        category_details = []
        for cat_name, target_pct in config.CATEGORY_WEIGHT_RATIO.items():
            actual_pct = category_ratio.get(cat_name, 0)
            diff = abs(actual_pct - target_pct)
            ok = diff <= config.CATEGORY_RATIO_TOLERANCE
            if not ok:
                category_pass = False
            category_details.append(f"{cat_name}: 目标{target_pct}%/实际{actual_pct:.1f}%(差{diff:.1f}%)")

        report_data.append(["【6. 大类重量比例】", "配置值", "推算值", "判定", "说明"])
        report_data.append(["  配置比例", config_ratio_str, ratio_str,
                            "通过" if category_pass else "不通过",
                            f"容差: ±{config.CATEGORY_RATIO_TOLERANCE}%"])
        report_data.append(["  实际占比", "", ratio_detail, "", ""])
        for detail in category_details:
            report_data.append([f"    {detail}"])
        results.append(["大类重量比例", "通过" if category_pass else "不通过",
                        "; ".join(category_details)])
        formula_data.append([
            "大类重量比例",
            "algorithm_test_dish.category1, algorithm_test_plan_item.cook_weight",
            "占比 = SUM(分类重量) / SUM(总重量) * 100%\n简化比例 = 各占比 / 最小占比",
            "排餐参数标准化 - 大类配比 - 重量比例"
        ])
        report_data.append([""])

        # ------------------------------------------------------------------
        # 7. 每日菜品数量 + 热门菜数量（已配置: CATEGORY_DISH_COUNT, CATEGORY_HOT_DISH_COUNT）
        # ------------------------------------------------------------------
        count_pass = True
        hot_count_pass = True
        count_details = []
        report_data.append(["【7. 每日菜品数量（按大类）】", "配置值", "推算值", "判定", "说明"])

        for category in ["大荤", "小荤", "素菜"]:
            actual_count = avg_category_count.get(category, 0)
            target_count = config.CATEGORY_DISH_COUNT.get(category, 0)
            actual_hot = avg_hot_dish.get(category, 0)
            target_hot = config.CATEGORY_HOT_DISH_COUNT.get(category, 0)

            count_ok = abs(actual_count - target_count) <= 1  # 允许1道偏差
            hot_ok = abs(actual_hot - target_hot) <= 1

            if not count_ok:
                count_pass = False
            if not hot_ok:
                hot_count_pass = False

            report_data.append([f"  {category}总数", f"{target_count}道", f"{actual_count:.0f}道",
                                "通过" if count_ok else "不通过", "允许偏差±1道"])
            report_data.append([f"  {category}热门菜", f"{target_hot}道", f"{actual_hot:.1f}道",
                                "通过" if hot_ok else "不通过", "允许偏差±1道"])

            # 小类分布
            cat_subcat = subcategory_stats[subcategory_stats["大类"] == category]
            if len(cat_subcat) > 0:
                subcat_str = "，".join([f"{row['小类']}({row['数量']})" for _, row in cat_subcat.iterrows()])
                report_data.append([f"    {category}小类分布", "", subcat_str, "", ""])

            count_details.append(f"{category}: 目标{target_count}/实际{actual_count}, 热门目标{target_hot}/实际{actual_hot:.1f}")

        results.append(["每日菜品数量", "通过" if count_pass else "不通过", "; ".join(count_details)])
        results.append(["热门菜数量", "通过" if hot_count_pass else "不通过", "; ".join(count_details)])
        formula_data.append([
            "每日菜品数量",
            "algorithm_test_dish.category1, algorithm_test_dish.category2",
            "COUNT(dish_name) GROUP BY 日期, 大类",
            "排餐参数标准化 - 大类配比 - 数量"
        ])
        report_data.append([""])

        # ------------------------------------------------------------------
        # 8. 非热门菜重复占比（已配置: NON_HOT_REPEAT_MAX_RATIO）
        # ------------------------------------------------------------------
        repeat_pass = repeat_ratio <= config.NON_HOT_REPEAT_MAX_RATIO

        report_data.append(["【8. 非热门菜重复次数占比】", "配置值", "推算值", "判定", "说明"])
        report_data.append(["  重复占比上限", f"<={config.NON_HOT_REPEAT_MAX_RATIO}%", f"{repeat_ratio:.2f}%",
                            "通过" if repeat_pass else "不通过",
                            f"推算值应<={config.NON_HOT_REPEAT_MAX_RATIO}%"])
        report_data.append(["  总重复次数", "", total_repeat, "", ""])
        report_data.append(["  非热门菜总排餐数", "", total_dish_slots, "", ""])
        results.append(["非热门菜重复占比", "通过" if repeat_pass else "不通过",
                        f"推算{repeat_ratio:.2f}% <= 上限{config.NON_HOT_REPEAT_MAX_RATIO}%"])
        formula_data.append([
            "非热门菜重复占比",
            "algorithm_test_dish.popular_flag, algorithm_test_plan_item",
            "重复占比 = SUM(MAX(0, 排餐次数-1)) / 非热门菜总排餐数 * 100%",
            "排餐参数标准化 - 非热门菜重复次数占比"
        ])
        report_data.append([""])

        # ------------------------------------------------------------------
        # 9. 菜品最低重量（已配置: MIN_DISH_WEIGHT）
        # ------------------------------------------------------------------
        min_weight_pass = min_dish_weight >= config.MIN_DISH_WEIGHT

        report_data.append(["【9. 菜品最低重量】", "配置值", "推算值", "判定", "说明"])
        report_data.append(["  最低重量", f">={config.MIN_DISH_WEIGHT}g", f"{min_dish_weight:.0f}g",
                            "通过" if min_weight_pass else "不通过",
                            f"推算值应>={config.MIN_DISH_WEIGHT}g"])
        results.append(["菜品最低重量", "通过" if min_weight_pass else "不通过",
                        f"最低{min_dish_weight:.0f}g >= {config.MIN_DISH_WEIGHT}g"])
        formula_data.append([
            "菜品最低重量",
            "algorithm_test_plan_item.cook_weight",
            "MIN(cook_weight)",
            "排餐参数标准化 - 菜品最低重量"
        ])
        report_data.append([""])

        # ------------------------------------------------------------------
        # 10. 菜品不连续间隔天数（已配置: MIN_INTERVAL_DAYS）
        # ------------------------------------------------------------------
        interval_pass = min_interval >= config.MIN_INTERVAL_DAYS

        report_data.append(["【10. 菜品不连续间隔天数】", "配置值", "推算值", "判定", "说明"])
        report_data.append(["  最小间隔天数", f">={config.MIN_INTERVAL_DAYS}天", f"{min_interval}天",
                            "通过" if interval_pass else "不通过",
                            f"推算值应>={config.MIN_INTERVAL_DAYS}天"])
        results.append(["菜品不连续间隔天数", "通过" if interval_pass else "不通过",
                        f"最小间隔{min_interval}天 >= {config.MIN_INTERVAL_DAYS}天"])
        formula_data.append([
            "菜品不连续间隔天数",
            "algorithm_test_plan_item.cook_date",
            "MIN(DATEDIFF(当前日期, 上次日期)) GROUP BY 菜名",
            "排餐参数标准化 - 菜品不连续间隔天数"
        ])
        report_data.append([""])

        # ------------------------------------------------------------------
        # 11. 连续排餐违规检查（规则: MIN_INTERVAL_DAYS >= 1 时不允许连续排餐）
        # ------------------------------------------------------------------
        consecutive_check = query1_data.copy()
        consecutive_check["日期"] = pd.to_datetime(consecutive_check["日期"])
        consecutive_check = consecutive_check.sort_values(["菜名", "日期"])
        consecutive_check["连续排餐标记"] = (
            (consecutive_check["菜名"] == consecutive_check["菜名"].shift(1))
            & (consecutive_check["日期"] - consecutive_check["日期"].shift(1) == pd.Timedelta(days=1))
        ).astype(int)
        violations = consecutive_check[consecutive_check["连续排餐标记"] == 1]
        consecutive_pass = len(violations) == 0

        report_data.append(["【11. 连续排餐违规检查】", "配置值", "推算值", "判定", "说明"])
        if consecutive_pass:
            report_data.append(["  检查结果", "不允许连续排餐", "无连续排餐", "通过", ""])
        else:
            report_data.append(["  检查结果", "不允许连续排餐", f"发现{len(violations)}条违规", "不通过", ""])
            for _, row in violations.head(10).iterrows():
                report_data.append([f"    违规菜品", "", f"{row['菜名']} - {row['日期'].strftime('%Y-%m-%d')}", "", ""])
        results.append(["连续排餐检查", "通过" if consecutive_pass else "不通过",
                        f"{len(violations)}条违规"])
        formula_data.append([
            "连续排餐检查",
            "algorithm_test_plan_item.cook_date, cook_name",
            "同菜品相邻日期差=1天则为违规",
            "排餐规则 - 规则12: 连续2天不可出现同一道菜"
        ])
        report_data.append([""])

        # ------------------------------------------------------------------
        # 12. 热门菜窗口期分析（展示，不做通过/不通过判定）
        # ------------------------------------------------------------------
        report_data.append(["【12. 热门菜窗口期分析】"])
        for dish, freq in hot_dish_freq.head(15).items():
            report_data.append([f"  {dish}", "", f"出现{freq}次", "", ""])
        formula_data.append([
            "热门菜窗口期",
            "algorithm_test_dish.popular_flag",
            "COUNT(日期) WHERE popular_flag='是' GROUP BY 菜名",
            "排餐参数标准化 - 菜品源数据 - 窗口周期内出现次数"
        ])
        report_data.append([""])

        # ==================================================================
        # 汇总判定表
        # ==================================================================
        report_data.append(["=" * 80])
        report_data.append(["验证结果汇总"])
        report_data.append(["=" * 80])
        report_data.append(["参数名称", "配置值", "推算值", "判定", "说明"])
        for r in results:
            report_data.append([f"  {r[0]}", "", "", r[1], r[2]])

        total_checks = len(results)
        passed_checks = sum(1 for r in results if r[1] == "通过")
        failed_checks = total_checks - passed_checks
        report_data.append([""])
        report_data.append([f"总计: {total_checks}项", "", f"通过: {passed_checks}项, 不通过: {failed_checks}项",
                            "全部通过" if failed_checks == 0 else f"有{failed_checks}项不通过", ""])

        # 创建DataFrame
        report_df = pd.DataFrame(report_data, columns=["参数名称", "配置值", "推算值", "判定", "说明"])
        formula_df = pd.DataFrame(formula_data, columns=["参数名称", "数据来源", "计算公式", "对应标准参数"])
        results_df = pd.DataFrame(results, columns=["参数名称", "判定结果", "详细说明"])

        # 创建每日汇总数据
        daily_summary = query2_with_weekday[["日期", "星期", "总重量", "总价格", "预估人数", "人均消耗重量", "人均消费金额"]].copy()
        daily_summary["日期"] = daily_summary["日期"].dt.strftime("%Y-%m-%d")

        # 创建大类每日占比
        category_pivot = category_data.pivot(index="日期", columns="菜品大类", values="分类总重量").fillna(0)
        category_pivot_pct = category_pivot.div(category_pivot.sum(axis=1), axis=0) * 100
        category_pivot_pct = category_pivot_pct.round(2)
        category_pivot_pct.insert(0, "日期", category_pivot_pct.index)
        category_pivot_pct["日期"] = pd.to_datetime(category_pivot_pct["日期"]).dt.strftime("%Y-%m-%d")

        # 导出到Excel（多Sheet）
        with pd.ExcelWriter(output_file) as writer:
            report_df.to_excel(writer, sheet_name="参数反推报告", index=False)
            results_df.to_excel(writer, sheet_name="验证结果汇总", index=False)
            daily_summary.to_excel(writer, sheet_name="每日汇总数据", index=False)
            category_pivot_pct.to_excel(writer, sheet_name="大类每日占比", index=False)
            formula_df.to_excel(writer, sheet_name="推算公式说明", index=False)

        logger.info(f"参数反推报告已成功导出到 {output_file}")

    except Exception as e:
        logger.error(f"发生错误: {e}")
        import traceback
        traceback.print_exc()


# ==================== 主要导出函数 ====================
def fetch_data_and_export2() -> None:
    """
    查询每天排餐菜品的总重量和总价格，并添加人均消耗菜品重量和人均消费金额列

    输出文件: output2.xlsx
    """
    output_file = get_output_path("output2.xlsx")

    try:
        with get_db_connection() as conn:
            data = pd.read_sql(get_query2(), conn)

        data = add_weekday_column(data)
        data = add_estimated_people_column(data)

        data["人均消耗重量"] = (data["总重量"] / data["预估人数"]).round(2)
        data["人均消费金额"] = (data["总价格"] / data["预估人数"]).round(2)

        data.to_excel(output_file, index=False)
        logger.info(f"数据已成功导出到 {output_file}")

    except Exception as e:
        logger.error(f"发生错误: {e}")


def fetch_data_and_export3() -> None:
    """
    综合分析：人均消耗+浮动校验+分类占比+热门菜+制作方式

    输出文件: output3.xlsx
    """
    output_file = get_output_path("output3.xlsx")

    try:
        with get_db_connection() as conn:
            # 查询基础数据
            data = pd.read_sql(get_query2(), conn)
            data = add_weekday_column(data)
            data = add_estimated_people_column(data)

            # 计算人均值
            data["人均消耗重量"] = (data["总重量"] / data["预估人数"]).round(2)
            data["总价格"] = data["总价格"].round(2)
            data["人均消费金额"] = (data["总价格"] / data["预估人数"]).round(2)

            # 计算浮动分析
            data = calculate_weight_analysis(data)
            data = calculate_price_analysis(data)

            # 分类占比汇总
            category_data = pd.read_sql(get_category_query(), conn)
            category_summary = calculate_category_summary(category_data)
            data = pd.merge(data, category_summary, on="日期", how="left")

            # 热门菜统计
            query1_data = pd.read_sql(get_query1(), conn)
            hot_summary = calculate_hot_dish_summary(query1_data)
            data = pd.merge(data, hot_summary, on="日期", how="left")

            # 制作方式比例
            cook_summary = calculate_cook_method_summary(query1_data)
            data = pd.merge(data, cook_summary, on="日期", how="left")

        data.to_excel(output_file, index=False)
        logger.info(f"数据已成功导出到 {output_file}")

    except Exception as e:
        logger.error(f"发生错误: {e}")


def fetch_all_results_and_export(plan_id: Optional[int] = None) -> None:
    """
    完整分析：多Sheet导出
    - Sheet1: 菜品重复率与连续排餐
    - Sheet2: 分类比例与制作方式
    - Sheet3: 细化分类汇总

    输出文件: output_all.xlsx
    """
    plan_id = plan_id or config.PLAN_ID
    output_file = get_output_path("output_all.xlsx")

    try:
        with get_db_connection() as conn:
            # 查询基础数据
            data = pd.read_sql(get_query1(plan_id), conn)
            data["日期"] = pd.to_datetime(data["日期"])

            # 添加星期列
            data = add_weekday_column(data)

            # 检查连续排餐
            data = check_consecutive_meals(data)

            # 计算重复比例
            data = calculate_repetition_rate(data)

            # Sheet1数据
            sheet1_data = data[["日期", "星期", "菜名", "重量", "连续排餐标记", "重复比例"]].copy()
            sheet1_data["日期"] = sheet1_data["日期"].dt.strftime("%Y-%m-%d")

            # 分类占比
            category_data = pd.read_sql(get_category_query(plan_id), conn)
            category_summary = calculate_category_summary(category_data)

            # 制作方式比例
            cook_summary = calculate_cook_method_summary(data)

            # 统一日期格式
            category_summary["日期"] = pd.to_datetime(category_summary["日期"]).dt.strftime("%Y-%m-%d")
            cook_summary["日期"] = pd.to_datetime(cook_summary["日期"]).dt.strftime("%Y-%m-%d")

            # Sheet2数据
            sheet2_data = pd.merge(
                category_summary[["日期", "分类占比汇总"]],
                cook_summary,
                on="日期",
                how="left",
            )

            # 细化分类
            detailed_data = pd.read_sql(get_detailed_category_query(plan_id), conn)
            detailed_data["日期"] = pd.to_datetime(detailed_data["日期"], errors="coerce")

            detailed_summary = (
                detailed_data.groupby(["日期", "菜品大类"])
                .apply(
                    lambda x: "，".join(
                        f"{row['细化分类']}({row['分类数量']})" for _, row in x.iterrows()
                    )
                )
                .reset_index(name="细化分类汇总")
            )
            detailed_summary["日期"] = detailed_summary["日期"].dt.strftime("%Y-%m-%d")

            # Sheet3数据
            sheet3_data = detailed_summary

        # 导出到Excel
        with pd.ExcelWriter(output_file) as writer:
            sheet1_data.to_excel(writer, sheet_name="菜品重复率与连续排餐", index=False)
            sheet2_data.to_excel(writer, sheet_name="分类比例与制作方式", index=False)
            sheet3_data.to_excel(writer, sheet_name="细化分类汇总", index=False)

        logger.info(f"所有结果已成功导出到 {output_file}")

    except Exception as e:
        logger.error(f"发生错误: {e}")


def fetch_data_and_export7() -> None:
    """
    每日热门菜统计

    输出文件: output7.xlsx
    """
    output_file = get_output_path("output7.xlsx")

    try:
        with get_db_connection() as conn:
            data = pd.read_sql(get_query1(), conn)
            data["日期"] = pd.to_datetime(data["日期"])

        hot_summary = calculate_hot_dish_summary(data)
        hot_summary["日期"] = pd.to_datetime(hot_summary["日期"]).dt.strftime("%Y-%m-%d")

        hot_summary.to_excel(output_file, index=False)
        logger.info(f"数据已成功导出到 {output_file}")

    except Exception as e:
        logger.error(f"发生错误: {e}")


def export_popular_rate_dish_count() -> None:
    """
    导出popular_rate不为0的菜品的排餐次数

    输出文件: popular_rate_dish_count.xlsx
    """
    output_file = get_output_path("popular_rate_dish_count.xlsx")

    try:
        with get_db_connection() as conn:
            data = pd.read_sql(get_popular_rate_query(), conn)

        data.to_excel(output_file, index=False)
        logger.info(f"数据已成功导出到 {output_file}")

    except Exception as e:
        logger.error(f"发生错误: {e}")


# ==================== 主程序 ====================
if __name__ == "__main__":
    # fetch_data_and_export2()
    fetch_data_and_export3()
    # fetch_data_and_export7()
    fetch_all_results_and_export()
    export_popular_rate_dish_count()

    # 参数反推验证报告（从排餐数据反推算法参数设置）
    reverse_engineer_parameters()
