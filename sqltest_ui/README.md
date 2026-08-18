# 智能排餐参数验证工具 - UI 界面

## 功能简介

提供 Streamlit 可视化界面，用于修改排餐参数并执行验证。

**支持两种使用方式**：
1. **命令行方式**：`python test_dir/sqltest.py`（使用代码中的默认配置）
2. **UI 界面方式**：通过网页表单修改参数（本工具）

---

## 安装依赖

```bash
pip install -r sqltest_ui/requirements.txt
```

---

## 启动 UI

```bash
streamlit run sqltest_ui/app.py
```

浏览器会自动打开 `http://localhost:8501`

---

## 目录结构

```
sqltest_ui/
├── __init__.py           # 模块初始化
├── app.py                # UI 主入口
├── config_manager.py     # 配置管理器
├── configs/              # 配置方案存储
│   └── default.json      # 默认配置
├── requirements.txt      # 依赖清单
└── README.md             # 本文件
```

---

## 配置方案管理

### 保存配置

在 UI 界面填写参数后，点击"保存配置"，输入方案名称即可保存。

### 加载配置

下拉选择已有配置方案，参数会自动填充到表单。

### 配置文件格式

配置保存为 JSON 文件，存放在 `configs/` 目录：

```json
{
    "name": "方案名称",
    "plan_id": 25080403,
    "db": { ... },
    "consumption": { ... },
    "category": { ... },
    "cook_method": { ... },
    "limits": { ... },
    "output": { ... }
}
```

---

## 无 UI 执行方式

不使用 UI 时，可直接编辑 `test_dir/sqltest.py` 中的 Config 类：

```python
# 在 test_dir/sqltest.py 中修改
PLAN_ID: int = 25090001
STANDARD_WEIGHT: float = 400.0
```

然后执行：

```bash
python test_dir/sqltest.py
```

---

## 功能按钮

| 按钮 | 功能 |
|------|------|
| 🚀 执行全部 | 依次执行所有导出函数（基础+综合+热门菜+完整+热门度） |
| 🔍 参数验证 | 执行参数反推验证（生成 parameter_verification.xlsx） |
| 📊 综合分析 | 执行综合分析（output3.xlsx） |
| 📋 完整分析 | 执行完整分析（output_all.xlsx，多Sheet） |
| 📈 基础分析 | 执行基础人均分析（output2.xlsx） |

## 界面说明

### 侧边栏

- **配置方案选择器**：下拉选择已保存的配置方案
- **保存/删除**：保存当前配置或删除选中的配置
- **参数配置区域**：
  - 排餐计划ID
  - 数据库配置（可折叠）
  - 消费配置（人均重量/价格、容差）
  - 大类配比（重量比例、菜品数量、热门菜数量）
  - 制作方式配比（炒菜机/蒸烤箱/人工比例）
  - 限制参数（重复上限、最低重量、间隔天数）
  - 输出配置（目录、时间戳开关）

### 主内容区

- **执行按钮组**：5个功能按钮，点击执行对应分析
- **执行日志**：实时显示执行过程和结果
- **输出文件列表**：展示最近生成的5个文件，提供下载

---

## 输出文件

所有生成的文件保存在 `reports/` 目录：

| 文件 | 说明 |
|------|------|
| `output2_*.xlsx` | 基础人均分析 |
| `output3_*.xlsx` | 综合分析 |
| `output7_*.xlsx` | 热门菜统计 |
| `output_all_*.xlsx` | 完整分析（多Sheet） |
| `parameter_verification_*.xlsx` | 参数反推验证报告 |
| `popular_rate_dish_count_*.xlsx` | 热门度分析 |

文件名包含时间戳，防止覆盖。
