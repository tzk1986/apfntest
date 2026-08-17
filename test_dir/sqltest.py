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
    """全局配置类"""

    # 数据库配置
    DB_HOST: str = "10.50.11.77"
    DB_USER: str = "root"
    DB_PASSWORD: str = "!@#$%^@2021@epfly"
    DB_NAME: str = "ifood_kitchen"
    DB_PORT: int = 3306

    # 排餐计划ID
    PLAN_ID: int = 25080403

    # 标准值配置
    STANDARD_WEIGHT: float = 350.0  # 标准人均消耗重量(g)
    WEIGHT_TOLERANCE: float = 0.02  # 重量浮动比例
    STANDARD_PRICE: float = 24.0  # 标准人均消费金额(元)
    PRICE_TOLERANCE: float = 0.04  # 价格浮动比例

    # 输出目录
    OUTPUT_DIR: str = r"d:\tangzk\py\seldom-web-testing\reports"

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
    """查询1：每天排餐菜品和重量数据"""
    plan_condition = build_plan_query(plan_id)
    return f"""SELECT
        m.cook_date AS 日期,
        d.dish_name AS 菜名,
        m.cook_weight AS 重量,
        d.price AS 50克价格,
        d.category1 AS 大类,
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
