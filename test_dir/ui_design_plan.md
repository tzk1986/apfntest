# sqltest.py UI 界面设计方案

## 1. 设计目标

- **保留原有功能**：sqltest.py 零改动，命令行执行方式不变
- **新增 UI 操作**：通过 Streamlit 提供可视化界面，方便修改参数
- **双模式共存**：命令行 / UI 两种方式使用同一份核心代码

---

## 2. 两种使用方式

### 方式A：命令行执行（原有方式，保持不变）

```bash
# 直接执行（使用 Config 类中的默认值）
python test_dir/sqltest.py
```

**修改参数**：手动编辑 `sqltest.py` 中的 Config 类

```python
# 在 sqltest.py 中修改
PLAN_ID: int = 25090001
STANDARD_WEIGHT: float = 400.0
WEIGHT_TOLERANCE: float = 0.03
```

### 方式B：UI 界面执行（新增方式）

```bash
# 启动 UI 服务
streamlit run test_dir/streamlit_app.py

# 浏览器自动打开 http://localhost:8501
# 在网页表单中修改参数 → 点击执行按钮
```

---

## 3. 架构设计

```
┌──────────────────────────────────────────────────────┐
│               浏览器 UI (streamlit_app.py)            │
│   ┌──────────────────────────────────────────────┐   │
│   │ 侧边栏表单：配置参数                          │   │
│   │ 主内容区：执行结果 + 下载链接                  │   │
│   └──────────────────────────────────────────────┘   │
└──────────────────────┬───────────────────────────────┘
                       │ 创建 Config 实例
                       ▼
┌──────────────────────────────────────────────────────┐
│              核心逻辑 (sqltest.py - 零改动)           │
│   ┌──────────────────────────────────────────────┐   │
│   │ Config 类（硬编码默认值）                      │   │
│   │ fetch_data_and_export2/3/7()                 │   │
│   │ fetch_all_results_and_export()               │   │
│   │ reverse_engineer_parameters()                │   │
│   └──────────────────────────────────────────────┘   │
└──────────────────────┬───────────────────────────────┘
                       ▼
┌──────────────────────────────────────────────────────┐
│              配置管理 (config_manager.py - 新增)       │
│   - 保存/加载配置方案（JSON）                         │
│   - 多套配置切换                                     │
└──────────────────────┬───────────────────────────────┘
                       ▼
                  ┌─────────┐
                  │  MySQL  │
                  └─────────┘
```

---

## 4. 目录结构设计

### 4.1 统一目录规划

```
D:/tangzk/py/seldom-web-testing/
├── file/                          # 文档和备份（已有，不动）
│   ├── sqltest.py.bak             # 原始代码备份
│   ├── sqltest_usage_guide.md     # V1使用说明
│   └── sqltest_usage_guide_v2.md  # V2使用说明
│
├── reports/                       # 输出目录（已有，不动）
│   └── *.xlsx                     # 生成的Excel文件
│
├── test_dir/                      # 核心逻辑（已有，不动）
│   └── sqltest.py                 # 核心代码（零改动）
│
└── sqltest_ui/                    # 新增：UI模块统一目录
    ├── __init__.py                # 模块初始化
    ├── app.py                     # UI主入口
    ├── config_manager.py          # 配置管理器
    ├── configs/                   # 配置方案存储目录
    │   └── default.json           # 默认配置
    ├── requirements.txt           # UI依赖清单
    └── README.md                  # UI使用说明
```

### 4.2 目录设计说明

| 目录 | 用途 | 说明 |
|------|------|------|
| `file/` | 文档备份 | 已有，存放备份和说明文档 |
| `reports/` | 输出目录 | 已有，存放生成的Excel文件 |
| `test_dir/` | 核心逻辑 | 已有，sqltest.py 保持不变 |
| `sqltest_ui/` | UI模块 | **新增**，所有UI相关文件集中存放 |

### 4.3 新增文件清单

| 文件路径 | 说明 |
|----------|------|
| `sqltest_ui/__init__.py` | 模块初始化文件 |
| `sqltest_ui/app.py` | Streamlit UI 主入口 |
| `sqltest_ui/config_manager.py` | 配置方案保存/加载管理器 |
| `sqltest_ui/configs/default.json` | 默认配置方案 |
| `sqltest_ui/requirements.txt` | UI 依赖清单 |
| `sqltest_ui/README.md` | UI 使用说明文档 |

**不修改的文件**：
- `test_dir/sqltest.py`（核心逻辑完全不变）

---

## 5. UI 界面设计

### 5.1 整体布局

```
┌──────────────────────────────────────────────────────────────┐
│  🍽️ 智能排餐参数验证工具          [配置方案▼] [保存] [加载]   │
├───────────────────────┬──────────────────────────────────────┤
│  侧边栏               │  主内容区                             │
│  ┌─────────────────┐ │  ┌──────────────────────────────────┐ │
│  │ 📋 配置模块      │ │  │ 📊 执行按钮                      │ │
│  │  □ 排餐计划      │ │  │ [执行全部] [参数验证] [综合分析] │ │
│  │  □ 消费配置      │ │  └──────────────────────────────────┘ │
│  │  □ 大类配比      │ │  ┌──────────────────────────────────┐ │
│  │  □ 制作方式      │ │  │ ✅ 验证结果汇总       通过 9/10  │ │
│  │  □ 限制参数      │ │  │ 人均消耗重量 ✅通过              │ │
│  │  □ 输出配置      │ │  │ 大类比例 ✅通过                  │ │
│  └─────────────────┘ │  │ ...                              │ │
│                       │  └──────────────────────────────────┘ │
│                       │  ┌──────────────────────────────────┐ │
│                       │  │ 📥 下载结果                       │ │
│                       │ │  [output2] [output3] [验证报告]   │ │
│                       │  └──────────────────────────────────┘ │
└───────────────────────┴──────────────────────────────────────┘
```

### 5.2 配置模块

| 模块 | 配置项 |
|------|--------|
| 排餐计划 | 计划ID |
| 消费配置 | 人均重量、浮动比例、人均金额、价格浮动比例 |
| 大类配比 | 可编辑表格（大类、重量占比、菜品数、热门菜数） |
| 制作方式 | 可编辑表格（方式、比例） |
| 限制参数 | 非热门菜重复上限、最低重量、间隔天数 |
| 输出配置 | 输出目录、是否启用时间戳 |

### 5.3 执行按钮

| 按钮 | 对应函数 |
|------|---------|
| [执行全部] | 依次执行所有导出函数 |
| [参数反推验证] | `reverse_engineer_parameters()` |
| [综合分析] | `fetch_data_and_export3()` |
| [完整分析] | `fetch_all_results_and_export()` |
| [基础分析] | `fetch_data_and_export2()` |
| [重置配置] | 恢复默认值 |

---

## 6. 配置方案管理

### 6.1 保存配置

用户可命名保存当前配置为方案：

```json
{
  "name": "25080403标准配置",
  "plan_id": 25080403,
  "std_weight": 350.0,
  "weight_tolerance": 0.02,
  "std_price": 24.0,
  "price_tolerance": 0.04,
  "category_ratio": {"大荤": 50, "小荤": 30, "素菜": 20},
  "category_dish_count": {"大荤": 8, "小荤": 7, "素菜": 4},
  "category_hot_count": {"大荤": 2, "小荤": 2, "素菜": 1},
  "cook_method_ratio": {"炒菜机": 8, "蒸烤箱": 6, "人工": 5},
  "non_hot_repeat_max": 20.0,
  "min_dish_weight": 50.0,
  "min_interval_days": 1
}
```

### 6.2 加载配置

下拉选择已有方案，自动填充表单。

---

## 7. 依赖安装

```bash
pip install streamlit
# 或
pip install -r test_dir/requirements_ui.txt
```

---

## 8. 实施步骤

| 步骤 | 任务 | 文件路径 |
|------|------|----------|
| 1 | 创建 UI 目录结构 | `sqltest_ui/` |
| 2 | 创建配置管理器骨架 | `sqltest_ui/config_manager.py` |
| 3 | 创建 UI 主入口骨架 | `sqltest_ui/app.py` |
| 4 | 创建默认配置 | `sqltest_ui/configs/default.json` |
| 5 | 创建依赖和说明文件 | `sqltest_ui/requirements.txt`、`README.md` |
| 6 | 实现配置管理器功能 | 填充 `config_manager.py` |
| 7 | 实现 UI 界面功能 | 填充 `app.py` |
| 8 | 测试两种执行方式 | 命令行 + UI |

---

## 9. 使用示例

### 9.1 命令行（无 UI）

```bash
# 1. 编辑参数（可选）
# 修改 test_dir/sqltest.py 中的 Config 类

# 2. 执行
python test_dir/sqltest.py

# 3. 查看结果
# 文件输出到 reports/ 目录
```

### 9.2 UI 界面

```bash
# 1. 安装依赖
pip install streamlit

# 2. 启动 UI
streamlit run test_dir/streamlit_app.py

# 3. 浏览器打开 http://localhost:8501

# 4. 在网页中：
#    - 填写/选择配置参数
#    - 点击执行按钮
#    - 下载结果文件
```

---

## 10. 文件路径汇总

| 文件 | 路径 | 状态 |
|------|------|------|
| 核心逻辑 | `test_dir/sqltest.py` | 已有，不动 |
| 备份 | `file/sqltest.py.bak` | 已有 |
| 使用说明V1 | `file/sqltest_usage_guide.md` | 已有 |
| 使用说明V2 | `file/sqltest_usage_guide_v2.md` | 已有 |
| 设计方案 | `test_dir/ui_design_plan.md` | 已有（本文件） |
| UI模块目录 | `sqltest_ui/` | **新增** |
| UI主入口 | `sqltest_ui/app.py` | **新增** |
| 配置管理器 | `sqltest_ui/config_manager.py` | **新增** |
| 默认配置 | `sqltest_ui/configs/default.json` | **新增** |
| UI依赖 | `sqltest_ui/requirements.txt` | **新增** |
| UI说明 | `sqltest_ui/README.md` | **新增** |

---

## 11. 接口设计（骨架文件）

### 11.1 config_manager.py 接口

```python
class ConfigManager:
    """配置方案管理器"""
    
    def __init__(self, configs_dir: str):
        """初始化，指定配置存储目录"""
        pass
    
    def list_configs(self) -> list[str]:
        """列出所有可用的配置方案名称"""
        pass
    
    def load_config(self, name: str) -> dict:
        """加载指定名称的配置方案"""
        pass
    
    def save_config(self, name: str, config_data: dict) -> None:
        """保存配置方案"""
        pass
    
    def delete_config(self, name: str) -> None:
        """删除配置方案"""
        pass
    
    def get_default_config(self) -> dict:
        """获取默认配置"""
        pass
    
    def config_to_sqltest_config(self, config_data: dict):
        """将配置dict转换为sqltest.py的Config对象"""
        pass
```

### 11.2 app.py 接口

```python
def main():
    """UI主入口"""
    pass

def render_sidebar():
    """渲染侧边栏：配置表单"""
    pass

def render_main_content():
    """渲染主内容区：执行按钮和结果展示"""
    pass

def execute_all(config):
    """执行所有导出函数"""
    pass

def execute_verification(config):
    """执行参数反推验证"""
    pass

def show_results():
    """展示执行结果和下载链接"""
    pass
```

---

**确认后开始实施。**
