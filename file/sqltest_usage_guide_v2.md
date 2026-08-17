# sqltest.py 使用说明文档（V2 优化版）

## 1. 概述

`sqltest.py` 是一个智能菜谱排餐数据查询与导出工具，用于连接数据库查询排餐计划数据，并将结果导出为 Excel 报表，方便比对排餐结果与算法设置是否一致。

### 1.1 版本特性（V2 优化版）

| 优化项 | 说明 |
|--------|------|
| **配置集中管理** | 使用 `Config` 数据类统一管理所有配置 |
| **日志系统** | 使用 `logging` 模块替代 `print`，带时间戳和级别 |
| **数据库连接** | 使用上下文管理器自动管理连接生命周期 |
| **SQL 模板化** | 所有 SQL 查询封装为函数，支持动态 `plan_id` 参数 |
| **函数拆分** | 数据处理逻辑拆分为独立函数，便于复用和测试 |
| **类型提示** | 添加完整的类型注解，提升代码可读性 |
| **路径处理** | 使用 `pathlib` 处理文件路径，自动创建输出目录 |

---

## 2. 环境依赖

```bash
pip install pymysql pandas
```

- **Python**: >= 3.7
- **pymysql**: 数据库连接
- **pandas**: 数据处理与 Excel 导出
- **数据库**: MySQL (`ifood_kitchen`)

---

## 3. 配置说明

### 3.1 Config 数据类

所有配置集中在 `Config` 类中（第 26-58 行）：

```python
@dataclass(frozen=True)
class Config:
    # ========== 数据库配置 ==========
    DB_HOST: str = "10.50.11.77"
    DB_USER: str = "root"
    DB_PASSWORD: str = "!@#$%^@2021@epfly"
    DB_NAME: str = "ifood_kitchen"
    DB_PORT: int = 3306

    # ========== 排餐计划ID ==========
    PLAN_ID: int = 25080403

    # ========== 消费配置（对应: 排餐参数标准化 - 3.消费配置） ==========
    STANDARD_WEIGHT: float = 350.0    # 人均消耗菜品重量(g)
    WEIGHT_TOLERANCE: float = 0.02    # 重量浮动比例（0-1之间）
    STANDARD_PRICE: float = 24.0      # 人均消费金额(元)
    PRICE_TOLERANCE: float = 0.04     # 价格浮动比例（0-1之间）

    # ========== 大类配比（对应: 排餐参数标准化 - 4.大类配比） ==========
    CATEGORY_WEIGHT_RATIO: dict = {"大荤": 50, "小荤": 30, "素菜": 20}  # 大类重量占比(%)
    CATEGORY_DISH_COUNT: dict = {"大荤": 8, "小荤": 7, "素菜": 4}        # 每日各大类菜品数量
    CATEGORY_HOT_DISH_COUNT: dict = {"大荤": 2, "小荤": 2, "素菜": 1}    # 每日各大类热门菜数量
    CATEGORY_RATIO_TOLERANCE: float = 5.0  # 大类比例判定容差(%)

    # ========== 制作方式配比（对应: 排餐参数标准化 - 5.制作方式配比） ==========
    COOK_METHOD_RATIO: dict = {"炒菜机": 8, "蒸烤箱": 6, "人工": 5}      # 制作方式目标比例
    COOK_METHOD_RATIO_TOLERANCE: float = 2.0  # 比例判定容差

    # ========== 非热门菜重复限制 ==========
    NON_HOT_REPEAT_MAX_RATIO: float = 20.0  # 非热门菜重复占比上限(%)

    # ========== 菜品最低重量 ==========
    MIN_DISH_WEIGHT: float = 50.0  # 单道菜品最低出品重量(g)

    # ========== 菜品不连续间隔天数 ==========
    MIN_INTERVAL_DAYS: int = 1  # 同一菜品最低间隔天数（0=不限, 1=不可连续）

    # ========== 输出配置 ==========
    OUTPUT_DIR: str = r"d:\tangzk\py\seldom-web-testing\reports"
    ENABLE_TIMESTAMP: bool = True  # 是否启用时间戳（防止文件覆盖）
```

### 3.2 修改配置示例

**修改排餐计划 ID**：
```python
# 方式1：直接修改 Config 类
PLAN_ID: int = 25080999  # 改为新的计划ID

# 方式2：运行时传参
fetch_all_results_and_export(plan_id=25080999)
```

**修改标准值**：
```python
STANDARD_WEIGHT: float = 400.0  # 调整为400g
STANDARD_PRICE: float = 30.0    # 调整为30元
```

### 3.3 常量配置

文件第 66-84 行定义了两个常量字典：

| 常量名 | 用途 |
|--------|------|
| `DAY_NAME_MAP` | 英文星期转中文映射 |
| `ESTIMATED_PEOPLE` | 各星期预估用餐人数 |

预估人数配置：
| 星期 | 预估人数 |
|------|----------|
| 星期一 | 300 |
| 星期二 | 280 |
| 星期三 | 280 |
| 星期四 | 280 |
| 星期五 | 250 |

---

## 4. 代码架构

### 4.1 文件结构

```
sqltest.py
├── 配置区域
│   ├── Config 数据类
│   └── 常量定义
├── 工具函数
│   ├── get_db_connection()        # 数据库连接上下文管理器
│   ├── get_output_path()          # 获取输出路径
│   ├── add_weekday_column()       # 添加星期列
│   └── add_estimated_people_column()  # 添加预估人数列
├── SQL 查询模板
│   ├── get_query1()               # 菜品明细查询
│   ├── get_query2()               # 每日汇总查询
│   ├── get_query3()               # 分类重量查询
│   ├── get_category_query()       # 分类占比查询
│   ├── get_detailed_category_query()  # 细化分类查询
│   └── get_popular_rate_query()   # 热门度查询
├── 数据处理函数
│   ├── calculate_category_summary()    # 分类占比汇总
│   ├── calculate_cook_method_summary() # 制作方式比例
│   ├── calculate_hot_dish_summary()    # 热门菜统计
│   ├── calculate_weight_analysis()     # 重量分析
│   ├── calculate_price_analysis()      # 价格分析
│   ├── calculate_repetition_rate()     # 重复率计算
│   └── check_consecutive_meals()       # 连续排餐检查
├── 主要导出函数
│   ├── fetch_data_and_export2()
│   ├── fetch_data_and_export3()
│   ├── fetch_all_results_and_export()
│   ├── fetch_data_and_export7()
│   └── export_popular_rate_dish_count()
└── 主程序入口
```

### 4.2 工具函数说明

| 函数 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `get_db_connection()` | 无 | Connection | 数据库连接上下文管理器 |
| `get_output_path(filename)` | 文件名 | Path | 返回完整输出路径，自动创建目录 |
| `add_weekday_column(df, date_col)` | DataFrame, 日期列名 | DataFrame | 添加中文星期列 |
| `add_estimated_people_column(df)` | DataFrame | DataFrame | 添加预估人数列 |
| `build_plan_query(plan_id)` | plan_id | str | 构建SQL过滤条件 |

---

## 5. 主要导出函数

### 5.1 fetch_data_and_export2()

**功能**：每日排餐总重量/总价格 + 人均消耗分析

**输出文件**：`output2.xlsx`

**输出列**：

| 列名 | 类型 | 说明 |
|------|------|------|
| 日期 | str | 排餐日期 |
| 总重量 | float | 当天所有菜品总重量(g) |
| 总价格 | float | 当天所有菜品总价格(元) |
| 星期 | str | 中文星期 |
| 预估人数 | int | 根据星期映射的用餐人数 |
| 人均消耗重量 | float | 总重量/预估人数(g) |
| 人均消费金额 | float | 总价格/预估人数(元) |

---

### 5.2 fetch_data_and_export3()

**功能**：综合分析（人均消耗 + 浮动校验 + 分类占比 + 热门菜 + 制作方式）

**输出文件**：`output3.xlsx`

**输出列**：

| 列名 | 类型 | 说明 |
|------|------|------|
| 日期 | str | 排餐日期 |
| 总重量 | float | 当天总重量(g) |
| 总价格 | float | 当天总价格(元) |
| 星期 | str | 中文星期 |
| 预估人数 | int | 预估用餐人数 |
| 人均消耗重量 | float | 人均重量(g) |
| 重量浮动范围 | str | 标准值±2%范围 |
| 重量浮动值 | float | 实际值-标准值 |
| 重量是否在范围内 | str | "在范围内"/"超出范围" |
| 人均消费金额 | float | 人均价格(元) |
| 价格浮动范围 | str | 标准值±4%范围 |
| 价格浮动值 | float | 实际值-标准值 |
| 价格是否在范围内 | str | "在范围内"/"超出范围" |
| 分类占比汇总 | str | （大荤:小荤:素菜）：XX%:XX%:XX% |
| 每日热门菜统计 | str | 大荤（N），小荤（N），素菜（N） |
| 制作方式比例 | str | （炒菜机:蒸烤箱:人工）：N:N:N |

---

### 5.3 fetch_all_results_and_export(plan_id)

**功能**：完整多Sheet分析导出

**输出文件**：`output_all.xlsx`

**参数**：
- `plan_id` (Optional[int]): 排餐计划ID，默认使用 config.PLAN_ID

**Sheet 1 - 菜品重复率与连续排餐**：

| 列名 | 类型 | 说明 |
|------|------|------|
| 日期 | str | YYYY-MM-DD |
| 星期 | str | 中文星期 |
| 菜名 | str | 菜品名称 |
| 重量 | float | 菜品重量(g) |
| 连续排餐标记 | int | 1=连续两天排餐，0=非连续 |
| 重复比例 | float | 当周重复次数/当周总次数 |

**Sheet 2 - 分类比例与制作方式**：

| 列名 | 类型 | 说明 |
|------|------|------|
| 日期 | str | YYYY-MM-DD |
| 分类占比汇总 | str | （大荤:小荤:素菜）：XX%:XX%:XX% |
| 制作方式比例 | str | （炒菜机:蒸烤箱:人工）：N:N:N |

**Sheet 3 - 细化分类汇总**：

| 列名 | 类型 | 说明 |
|------|------|------|
| 日期 | str | YYYY-MM-DD |
| 菜品大类 | str | 大荤/小荤/素菜 |
| 细化分类汇总 | str | 细化分类1(N)，细化分类2(N) |

---

### 5.4 fetch_data_and_export7()

**功能**：每日热门菜统计

**输出文件**：`output7.xlsx`

**输出列**：

| 列名 | 类型 | 说明 |
|------|------|------|
| 日期 | str | YYYY-MM-DD |
| 每日热门菜统计 | str | 大荤（N），小荤（N），素菜（N） |

---

### 5.5 export_popular_rate_dish_count()

**功能**：热门度与排餐次数关联分析

**输出文件**：`popular_rate_dish_count.xlsx`

**输出列**：

| 列名 | 类型 | 说明 |
|------|------|------|
| 菜名 | str | 菜品名称 |
| 热门度 | float | 菜品热门度数值（>0） |
| 排餐次数 | int | 在计划中的排餐次数 |

---

## 6. 数据处理函数

### 6.1 calculate_category_summary(df)

计算分类占比汇总，输出格式：`（大荤:小荤:素菜）：XX.XX%:XX.XX%:XX.XX%`

### 6.2 calculate_cook_method_summary(df)

计算制作方式比例，输出格式：`（炒菜机:蒸烤箱:人工）：N:N:N`

### 6.3 calculate_hot_dish_summary(df)

统计每日热门菜数量（热门菜="是"），按大类分组汇总。

### 6.4 calculate_weight_analysis(df)

计算重量相关指标：
- 重量浮动范围：标准值 ± 2%
- 重量浮动值：实际值 - 标准值
- 是否在范围内：判断标记

### 6.5 calculate_price_analysis(df)

计算价格相关指标：
- 价格浮动范围：标准值 ± 4%
- 价格浮动值：实际值 - 标准值
- 是否在范围内：判断标记

### 6.6 calculate_repetition_rate(df)

计算菜品重复排餐比例：
- 按周统计每个菜品的排餐次数
- 重复次数 = 排餐次数 - 1
- 重复比例 = 重复次数 / 当周总排餐次数

### 6.7 check_consecutive_meals(df)

标记连续排餐的菜品：
- 按菜名和日期排序
- 如果同一菜品连续两天排餐，标记为1

---

## 7. 使用方法

### 7.1 基本使用

```bash
# 运行脚本
python test_dir/sqltest.py
```

### 7.2 选择执行函数

编辑文件末尾的主程序区域：

```python
if __name__ == "__main__":
    fetch_data_and_export2()              # 基础人均分析
    # fetch_data_and_export3()            # 综合分析
    # fetch_data_and_export7()            # 热门菜统计
    # fetch_all_results_and_export()      # 完整多Sheet分析
    # export_popular_rate_dish_count()    # 热门度分析
```

### 7.3 动态传入 plan_id

```python
# 在代码中调用
fetch_all_results_and_export(plan_id=25090001)
```

### 7.4 作为模块导入

```python
from test_dir.sqltest import (
    Config,
    get_query1,
    fetch_data_and_export2,
    calculate_category_summary,
)

# 修改配置
config = Config(PLAN_ID=25090001)

# 使用函数
sql = get_query1(plan_id=25090001)
fetch_data_and_export2()
```

---

## 8. 输出文件汇总

### 8.1 文件名规则

默认启用时间戳（`ENABLE_TIMESTAMP: bool = True`），文件名格式：
```
{原名}_{plan_id}_{YYYYMMDD_HHMMSS}.xlsx
```

**示例**：
```
output2_25080403_20260817_103015.xlsx
output3_25080403_20260817_103015.xlsx
output_all_25080403_20260817_103015.xlsx
parameter_verification_25080403_20260817_103015.xlsx
```

如需关闭时间戳（恢复固定文件名），修改配置：
```python
ENABLE_TIMESTAMP: bool = False
```

### 8.2 输出文件列表

| 原文件名 | 对应函数 | 主要内容 |
|----------|----------|----------|
| `output2.xlsx` | `fetch_data_and_export2()` | 每日总重量/总价格 + 人均消耗 |
| `output3.xlsx` | `fetch_data_and_export3()` | 综合分析（浮动校验+分类+热门+制作方式） |
| `output7.xlsx` | `fetch_data_and_export7()` | 每日热门菜统计 |
| `output_all.xlsx` | `fetch_all_results_and_export()` | 完整分析（3个Sheet） |
| `popular_rate_dish_count.xlsx` | `export_popular_rate_dish_count()` | 热门度与排餐次数关联 |
| `parameter_verification.xlsx` | `reverse_engineer_parameters()` | 参数反推验证报告（5个Sheet） |

输出目录：`d:\tangzk\py\seldom-web-testing\reports\`

---

## 9. 参数反推验证功能

### 9.1 功能说明

`reverse_engineer_parameters()` 函数可以从排餐数据中反推出算法的参数设置，生成参数验证报告，用于与标准参数文档（`排餐参数标准化整理.xlsx`）进行比对验证。

程序会**自动对比 Config 中的配置值与推算值**，输出"通过/不通过"判定结果。

### 9.2 反推参数及判定规则

| 序号 | 参数名称 | 计算公式 | 判定规则 |
|------|----------|----------|----------|
| 1 | 排餐天数 | `COUNT(DISTINCT cook_date)` | 仅展示，不判定 |
| 2 | 就餐人数 | 根据星期映射 | 仅展示，不判定 |
| 3 | 人均消耗重量 | `SUM(cook_weight) / 预估人数` | 均值在 [350*(1±0.02)] 内 且 每天不超出范围 |
| 4 | 重量浮动比例 | `MAX(\|实际值-均值\|/均值)` | 推算值 <= 配置值 + 0.005 |
| 5 | 人均消费金额 | `SUM((weight/50)*price) / 人数` | 均值在 [24*(1±0.04)] 内 且 每天不超出范围 |
| 6 | 价格浮动比例 | `MAX(\|实际值-均值\|/均值)` | 推算值 <= 配置值 + 0.005 |
| 7 | 大类重量比例 | `SUM(分类重量)/SUM(总重量)*100%` | 实际占比与配置偏差 <= 5% |
| 8 | 制作方式比例 | `COUNT GROUP BY 制作方式` | 简化比例与配置偏差 <= 2 |
| 9 | 每日菜品数量 | `COUNT GROUP BY 大类` | 实际数量与配置偏差 <= 1道 |
| 10 | 热门菜数量 | `COUNT WHERE popular_flag='是'` | 实际数量与配置偏差 <= 1道 |
| 11 | 非热门菜重复占比 | `SUM(MAX(0,次数-1))/总数*100%` | 推算值 <= 20% |
| 12 | 菜品最低重量 | `MIN(cook_weight)` | 推算值 >= 50g |
| 13 | 不连续间隔天数 | `MIN(DATEDIFF(相邻日期))` | 推算值 >= 1天 |
| 14 | 连续排餐检查 | 同菜品相邻日期差=1天则违规 | 违规数必须为0 |

### 9.3 输出文件说明

**文件名**: `parameter_verification_{plan_id}_{timestamp}.xlsx`（启用时间戳）

**Sheet 1 - 参数反推报告**:
每项参数包含 5 列：`参数名称 | 配置值 | 推算值 | 判定 | 说明`

```
================================================================================
排餐参数反推验证报告
排餐计划ID: 25080403
================================================================================

参数名称                          配置值          推算值              判定      说明
【3. 人均消耗菜品重量】
  标准人均重量                    350.0g          348.57g             通过      允许范围: 343.00-357.00g
  重量浮动比例                    0.02            0.0158              通过      推算值应<=配置值+0.005
  每日均在范围内                  0天超出         0天超出             通过      共5天排餐

【6. 大类重量比例】
  配置比例                        50%:30%:20%     5:3:2               通过      容差: ±5.0%
    大荤: 目标50%/实际48.5%(差1.5%)
    小荤: 目标30%/实际31.2%(差1.2%)
    素菜: 目标20%/实际20.3%(差0.3%)

验证结果汇总
参数名称              判定结果    详细说明
  人均消耗重量                   通过       均值348.6g, 浮动0.0158
  人均消费金额                   通过       均值23.85元, 浮动0.035
  大类重量比例                   通过       偏差均在5%内
  制作方式比例                   通过       偏差<=2
  每日菜品数量                   通过       偏差<=1道
  ...
总计: 10项                      通过: 9项, 不通过: 1项
```

**Sheet 2 - 验证结果汇总**（新增）:

所有验证项的判定结果汇总，便于快速查看整体情况：

| 参数名称 | 判定结果 | 详细说明 |
|----------|----------|----------|
| 人均消耗重量 | 通过 | 均值348.6g, 浮动0.0158 |
| 大类重量比例 | 不通过 | 大荤: 目标50%/实际42.3%(差7.7%) |
| ... | ... | ... |

**Sheet 3 - 每日汇总数据**:
| 日期 | 星期 | 总重量 | 总价格 | 预估人数 | 人均消耗重量 | 人均消费金额 |
|------|------|--------|--------|----------|--------------|--------------|

**Sheet 4 - 大类每日占比**:
| 日期 | 大荤 | 小荤 | 素菜 |
|------|------|------|------|

**Sheet 5 - 推算公式说明**:
| 参数名称 | 数据来源 | 计算公式 | 对应标准参数 |
|----------|----------|----------|--------------|
| 排餐天数 | cook_date | COUNT(DISTINCT cook_date) | 排餐周期配置 - 天序号 |
| ... | ... | ... | ... |

### 9.4 使用方法

```python
# 方式1：直接运行（主程序已包含）
python test_dir/sqltest.py

# 方式2：单独调用
from test_dir.sqltest import reverse_engineer_parameters
reverse_engineer_parameters()  # 使用默认 PLAN_ID
reverse_engineer_parameters(plan_id=25090001)  # 指定 PLAN_ID
```

### 9.5 修改验证标准

所有验证标准都在 `Config` 类中配置，修改后重新运行即可生效：

```python
# 修改人均重量标准
STANDARD_WEIGHT: float = 400.0    # 改为 400g
WEIGHT_TOLERANCE: float = 0.03    # 浮动比例放宽到 3%

# 修改大类配比目标
CATEGORY_WEIGHT_RATIO: dict = {"大荤": 45, "小荤": 35, "素菜": 20}

# 修改非热门菜重复上限
NON_HOT_REPEAT_MAX_RATIO: float = 25.0  # 放宽到 25%
```

### 9.6 与标准参数文档对比

反推报告生成后，可与 `排餐参数标准化整理.xlsx` 中的 `测试参数示例` Sheet 进行对比：

| 标准参数示例 | 反推报告对应项 |
|--------------|----------------|
| 就餐人数 300,280,280,280,250 | 【2. 每日就餐人数】 |
| 人均消耗菜品重量：350g | 【3. 人均消耗菜品重量】推算平均值 |
| 浮动比例：0.02 | 【3. 人均消耗菜品重量】推算浮动比例 |
| 人均消费金额：24元 | 【4. 人均消费金额】推算平均值 |
| 浮动比例：0.04 | 【4. 人均消费金额】推算浮动比例 |
| 制作方式比例 8:6:5 | 【5. 制作方式比例】推算比例 |
| 大类重量比例 5:3:2 | 【6. 大类重量比例】推算比例 |
| 大荤：总数8道，热门：2 | 【7. 每日菜品数量】大荤 |
| 非热门菜重复次数占比：20% | 【8. 非热门菜重复次数占比】推算占比 |
| 菜品最低重量：2000g | 【9. 菜品最低重量】推算最低重量 |
| 菜品不连续间隔天数：1 | 【10. 菜品不连续间隔天数】推算最小间隔 |

---

## 10. 日志输出示例

```
2026-08-17 10:30:15,123 - INFO - 数据库连接成功
2026-08-17 10:30:16,456 - INFO - 数据已成功导出到 d:\tangzk\py\seldom-web-testing\reports\output3.xlsx
2026-08-17 10:30:16,789 - INFO - 数据库连接已关闭
```

---

## 11. 扩展开发

### 10.1 添加新的导出函数

```python
def export_custom_report() -> None:
    """自定义报表导出"""
    output_file = get_output_path("custom_report.xlsx", plan_id=config.PLAN_ID)
    
    try:
        with get_db_connection() as conn:
            data = pd.read_sql("SELECT ...", conn)
        
        # 数据处理
        data = add_weekday_column(data)
        
        data.to_excel(output_file, index=False)
        logger.info(f"数据已成功导出到 {output_file}")
    
    except Exception as e:
        logger.error(f"发生错误: {e}")
```

### 10.2 添加新的 SQL 查询

```python
def get_custom_query(plan_id: Optional[int] = None) -> str:
    """自定义查询"""
    plan_condition = build_plan_query(plan_id)
    return f"""SELECT ... FROM ... WHERE {plan_condition}"""
```

### 10.3 添加新的数据处理函数

```python
def calculate_custom_metric(df: pd.DataFrame) -> pd.DataFrame:
    """计算自定义指标"""
    df = df.copy()
    # 处理逻辑
    return df
```

---

## 12. 注意事项

1. **数据库连接**：确保 `10.50.11.77:3306` 可访问
2. **输出目录**：程序会自动创建 `reports/` 目录
3. **预估人数**：仅配置了周一至周五，周末数据可能缺失
4. **标准值调整**：修改 `Config` 类中的 `STANDARD_WEIGHT` 和 `STANDARD_PRICE`
5. **plan_id 传参**：函数级传参优先级高于全局配置

---

## 13. 故障排查

| 错误信息 | 可能原因 | 解决方法 |
|----------|----------|----------|
| 数据库连接成功 后报错 | SQL语法错误 | 检查 SQL 查询语句 |
| 数据中未找到 '日期' 列 | 查询返回字段不匹配 | 检查 SQL 查询的列别名 |
| Permission denied | 输出目录无权限 | 以管理员身份运行或修改 OUTPUT_DIR |
| 预估人数列为空 | 周末数据 | 在 ESTIMATED_PEOPLE 中添加周末配置 |

---

## 14. 版本对比

| 项目 | V1 版本 | V2 优化版 |
|------|---------|-----------|
| 代码行数 | ~820行 | ~560行 |
| 配置方式 | 分散变量 | Config 数据类 |
| 日志系统 | print | logging |
| 数据库连接 | 每个函数重复管理 | 上下文管理器 |
| SQL 查询 | 字符串拼接 | 模板函数 |
| 路径处理 | 硬编码字符串 | pathlib |
| 类型提示 | 无 | 完整注解 |
| 函数复用 | 低 | 高 |
