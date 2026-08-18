# 快速启动指南

## 1. 启动 UI 界面

在项目根目录执行：

```bash
streamlit run sqltest_ui/app.py
```

浏览器会自动打开 `http://localhost:8501`

## 2. 使用流程

### 方式一：使用默认配置
1. 界面启动后自动加载默认配置
2. 直接点击功能按钮执行分析

### 方式二：修改参数
1. 在左侧边栏修改参数
2. 点击"保存"创建新配置方案
3. 点击功能按钮执行分析

### 方式三：加载已有配置
1. 在"选择配置方案"下拉框选择已有方案
2. 参数会自动填充
3. 可根据需要修改后执行

## 3. 功能按钮说明

- **🚀 执行全部**：执行所有5种分析（推荐）
- **🔍 参数验证**：反推验证参数是否正确
- **📊 综合分析**：生成 output3.xlsx
- **📋 完整分析**：生成 output_all.xlsx（多Sheet）
- **📈 基础分析**：生成 output2.xlsx

## 4. 查看结果

执行完成后，在"输出文件"区域可以：
- 查看最新生成的5个文件
- 点击下载按钮下载文件

## 5. 无 UI 执行方式

如果不想使用 UI，可以直接修改 `test_dir/sqltest.py` 中的 Config 类：

```python
@dataclass(frozen=True)
class Config:
    PLAN_ID: int = 25080403
    STANDARD_WEIGHT: float = 350.0
    # ... 其他参数
```

然后执行：

```bash
python test_dir/sqltest.py
```

## 6. 常见问题

### Q: 端口被占用怎么办？
A: 使用 `streamlit run sqltest_ui/app.py --server.port 8502`

### Q: 如何查看执行日志？
A: 执行按钮下方会实时显示执行日志

### Q: 文件保存在哪里？
A: 默认保存在 `d:\tangzk\py\seldom-web-testing\reports` 目录

### Q: 文件名中的时间戳是什么？
A: 格式为 `文件名_计划ID_YYYYMMDD_HHMMSS.xlsx`，防止文件覆盖
