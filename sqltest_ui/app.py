"""
智能排餐参数验证工具 - Streamlit UI 主入口

使用方法:
    streamlit run sqltest_ui/app.py
"""

import sys
import logging
from pathlib import Path
from datetime import datetime

# 添加项目根目录到路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

import streamlit as st
import pandas as pd

from config_manager import get_config_manager

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


def main():
    """UI主入口"""
    # 初始化配置管理器
    config_manager = get_config_manager()

    # 渲染侧边栏
    config_data = render_sidebar(config_manager)

    # 渲染主内容区
    render_main_content(config_data, config_manager)


def render_sidebar(config_manager):
    """
    渲染侧边栏：配置表单

    Args:
        config_manager: 配置管理器实例

    Returns:
        配置数据字典
    """
    st.sidebar.title("🍽️ 配置管理")

    # 配置方案选择器
    configs = config_manager.list_configs()
    selected_config = st.sidebar.selectbox(
        "选择配置方案",
        options=[""] + configs,
        format_func=lambda x: "新建配置" if x == "" else x,
    )

    # 加载配置
    if selected_config:
        config_data = config_manager.load_config(selected_config)
        st.sidebar.success(f"已加载: {selected_config}")
    else:
        config_data = config_manager.get_default_config()

    # 保存/删除按钮
    col1, col2 = st.sidebar.columns(2)
    with col1:
        save_name = st.text_input("保存为", value=selected_config or "新方案")
        if st.button("💾 保存", use_container_width=True):
            if save_name:
                config_data["name"] = save_name
                config_manager.save_config(save_name, config_data)
                st.sidebar.success(f"已保存: {save_name}")
                st.rerun()
    with col2:
        if selected_config and st.button("🗑️ 删除", use_container_width=True):
            if config_manager.delete_config(selected_config):
                st.sidebar.success(f"已删除: {selected_config}")
                st.rerun()

    st.sidebar.divider()

    # 排餐计划配置
    st.sidebar.subheader("排餐计划")
    config_data["plan_id"] = st.sidebar.number_input(
        "排餐计划ID",
        value=config_data.get("plan_id", 25080403),
        step=1,
        format="%d",
    )

    # 数据库配置
    with st.sidebar.expander("数据库配置", expanded=False):
        db_config = config_data.get("db", {})
        config_data["db"] = {
            "host": st.text_input("主机", value=db_config.get("host", "10.50.11.77")),
            "port": st.number_input("端口", value=db_config.get("port", 3306), step=1),
            "user": st.text_input("用户名", value=db_config.get("user", "root")),
            "password": st.text_input(
                "密码",
                value=db_config.get("password", ""),
                type="password",
            ),
            "database": st.text_input(
                "数据库",
                value=db_config.get("database", "ifood_kitchen"),
            ),
        }

    # 消费配置
    with st.sidebar.expander("消费配置", expanded=True):
        consumption = config_data.get("consumption", {})
        config_data["consumption"] = {
            "std_weight": st.number_input(
                "人均重量(g)",
                value=float(consumption.get("std_weight", 350.0)),
                step=10.0,
            ),
            "weight_tolerance": st.number_input(
                "重量容差",
                value=float(consumption.get("weight_tolerance", 0.02)),
                step=0.01,
                format="%.2f",
            ),
            "std_price": st.number_input(
                "人均价格(元)",
                value=float(consumption.get("std_price", 24.0)),
                step=1.0,
            ),
            "price_tolerance": st.number_input(
                "价格容差",
                value=float(consumption.get("price_tolerance", 0.04)),
                step=0.01,
                format="%.2f",
            ),
        }

    # 大类配比
    with st.sidebar.expander("大类配比", expanded=True):
        category = config_data.get("category", {})

        st.markdown("**重量比例(%)**")
        weight_ratio = category.get("weight_ratio", {})
        col1, col2, col3 = st.columns(3)
        with col1:
            dh_ratio = st.number_input(
                "大荤",
                value=int(weight_ratio.get("大荤", 50)),
                step=5,
            )
        with col2:
            xh_ratio = st.number_input(
                "小荤",
                value=int(weight_ratio.get("小荤", 30)),
                step=5,
            )
        with col3:
            sc_ratio = st.number_input(
                "素菜",
                value=int(weight_ratio.get("素菜", 20)),
                step=5,
            )

        st.markdown("**菜品数量**")
        dish_count = category.get("dish_count", {})
        col1, col2, col3 = st.columns(3)
        with col1:
            dh_count = st.number_input(
                "大荤",
                value=int(dish_count.get("大荤", 8)),
                step=1,
                key="dh_count",
            )
        with col2:
            xh_count = st.number_input(
                "小荤",
                value=int(dish_count.get("小荤", 7)),
                step=1,
                key="xh_count",
            )
        with col3:
            sc_count = st.number_input(
                "素菜",
                value=int(dish_count.get("素菜", 4)),
                step=1,
                key="sc_count",
            )

        st.markdown("**热门菜数量**")
        hot_count = category.get("hot_dish_count", {})
        col1, col2, col3 = st.columns(3)
        with col1:
            dh_hot = st.number_input(
                "大荤",
                value=int(hot_count.get("大荤", 2)),
                step=1,
                key="dh_hot",
            )
        with col2:
            xh_hot = st.number_input(
                "小荤",
                value=int(hot_count.get("小荤", 2)),
                step=1,
                key="xh_hot",
            )
        with col3:
            sc_hot = st.number_input(
                "素菜",
                value=int(hot_count.get("素菜", 1)),
                step=1,
                key="sc_hot",
            )

        config_data["category"] = {
            "weight_ratio": {"大荤": dh_ratio, "小荤": xh_ratio, "素菜": sc_ratio},
            "dish_count": {"大荤": dh_count, "小荤": xh_count, "素菜": sc_count},
            "hot_dish_count": {"大荤": dh_hot, "小荤": xh_hot, "素菜": sc_hot},
            "ratio_tolerance": st.number_input(
                "比例容差(%)",
                value=float(category.get("ratio_tolerance", 5.0)),
                step=1.0,
            ),
        }

    # 制作方式配比
    with st.sidebar.expander("制作方式配比", expanded=False):
        cook_method = config_data.get("cook_method", {})
        ratio = cook_method.get("ratio", {})

        col1, col2, col3 = st.columns(3)
        with col1:
            cjc = st.number_input("炒菜机", value=int(ratio.get("炒菜机", 8)), step=1)
        with col2:
            zk = st.number_input("蒸烤箱", value=int(ratio.get("蒸烤箱", 6)), step=1)
        with col3:
            rg = st.number_input("人工", value=int(ratio.get("人工", 5)), step=1)

        config_data["cook_method"] = {
            "ratio": {"炒菜机": cjc, "蒸烤箱": zk, "人工": rg},
            "tolerance": st.number_input(
                "容差",
                value=float(cook_method.get("tolerance", 2.0)),
                step=0.5,
            ),
        }

    # 限制参数
    with st.sidebar.expander("限制参数", expanded=False):
        limits = config_data.get("limits", {})
        config_data["limits"] = {
            "non_hot_repeat_max_ratio": st.number_input(
                "非热门菜重复上限(%)",
                value=float(limits.get("non_hot_repeat_max_ratio", 20.0)),
                step=5.0,
            ),
            "min_dish_weight": st.number_input(
                "最低菜品重量(g)",
                value=float(limits.get("min_dish_weight", 50.0)),
                step=10.0,
            ),
            "min_interval_days": st.number_input(
                "间隔天数",
                value=int(limits.get("min_interval_days", 1)),
                step=1,
            ),
        }

    # 输出配置
    with st.sidebar.expander("输出配置", expanded=False):
        output = config_data.get("output", {})
        config_data["output"] = {
            "dir": st.text_input(
                "输出目录",
                value=output.get("dir", r"d:\tangzk\py\seldom-web-testing\reports"),
            ),
            "enable_timestamp": st.checkbox(
                "启用时间戳",
                value=output.get("enable_timestamp", True),
            ),
        }

    return config_data


def render_main_content(config_data: dict, config_manager):
    """
    渲染主内容区：执行按钮和结果展示

    Args:
        config_data: 配置数据字典
        config_manager: 配置管理器实例
    """
    st.title("智能排餐参数验证工具")

    # 执行按钮组
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        if st.button("🚀 执行全部", use_container_width=True, type="primary"):
            execute_all(config_data, config_manager)

    with col2:
        if st.button("🔍 参数验证", use_container_width=True):
            execute_verification(config_data, config_manager)

    with col3:
        if st.button("📊 综合分析", use_container_width=True):
            execute_comprehensive(config_data, config_manager)

    with col4:
        if st.button("📋 完整分析", use_container_width=True):
            execute_full_analysis(config_data, config_manager)

    with col5:
        if st.button("📈 基础分析", use_container_width=True):
            execute_basic_analysis(config_data, config_manager)

    st.divider()

    # 执行日志
    if "execution_log" in st.session_state:
        st.subheader("执行日志")
        for log_entry in st.session_state.execution_log:
            if log_entry["level"] == "INFO":
                st.info(log_entry["message"])
            elif log_entry["level"] == "ERROR":
                st.error(log_entry["message"])
            else:
                st.write(log_entry["message"])

    # 展示验证结果
    if "verification_result" in st.session_state:
        st.divider()
        st.subheader("📋 参数验证结果")

        df = st.session_state.verification_result

        # 统计通过/不通过
        if "验证结果" in df.columns:
            pass_count = (df["验证结果"] == "通过").sum()
            fail_count = (df["验证结果"] == "不通过").sum()
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("总参数项", len(df))
            with col2:
                st.metric("✅ 通过", pass_count)
            with col3:
                st.metric("❌ 不通过", fail_count)

        # 展示完整表格
        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True,
        )

        # 下载按钮
        if "verification_file" in st.session_state:
            file_path = Path(st.session_state.verification_file)
            with open(file_path, "rb") as f:
                st.download_button(
                    "📥 下载验证报告",
                    data=f.read(),
                    file_name=file_path.name,
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                )

    # 展示结果
    show_results()


def set_sqltest_config(config_data: dict, config_manager):
    """
    设置 sqltest 模块的全局配置

    Args:
        config_data: 配置数据字典
        config_manager: 配置管理器实例

    Returns:
        sqltest 模块
    """
    # 确保 test_dir 在 Python 路径中
    test_dir = project_root / "test_dir"
    if str(test_dir) not in sys.path:
        sys.path.insert(0, str(test_dir))

    import sqltest

    # 转换为 Config 对象并设置
    config = config_manager.config_to_sqltest_config(config_data)
    sqltest.config = config
    return sqltest


def add_log(message: str, level: str = "INFO"):
    """添加执行日志"""
    if "execution_log" not in st.session_state:
        st.session_state.execution_log = []
    st.session_state.execution_log.append({
        "message": message,
        "level": level,
        "timestamp": datetime.now().strftime("%H:%M:%S"),
    })


def execute_all(config_data: dict, config_manager):
    """
    执行所有导出函数

    Args:
        config_data: 配置数据字典
        config_manager: 配置管理器实例
    """
    st.session_state.execution_log = []
    add_log("开始执行全部分析...")

    try:
        sqltest = set_sqltest_config(config_data, config_manager)

        add_log("执行基础分析 (output2)...")
        sqltest.fetch_data_and_export2()

        add_log("执行综合分析 (output3)...")
        sqltest.fetch_data_and_export3()

        add_log("执行热门菜统计 (output7)...")
        sqltest.fetch_data_and_export7()

        add_log("执行完整分析 (output_all)...")
        sqltest.fetch_all_results_and_export(config_data["plan_id"])

        add_log("执行热门度分析...")
        sqltest.export_popular_rate_dish_count()

        add_log("✅ 全部执行完成！")
        st.success("全部执行完成！")

    except Exception as e:
        add_log(f"❌ 执行失败: {str(e)}", "ERROR")
        st.error(f"执行失败: {str(e)}")


def execute_verification(config_data: dict, config_manager):
    """
    执行参数反推验证

    Args:
        config_data: 配置数据字典
        config_manager: 配置管理器实例
    """
    st.session_state.execution_log = []
    add_log("开始参数反推验证...")

    try:
        sqltest = set_sqltest_config(config_data, config_manager)
        sqltest.reverse_engineer_parameters(config_data["plan_id"])

        # 读取生成的验证文件
        reports_dir = project_root / "reports"
        verification_files = sorted(
            reports_dir.glob(f"parameter_verification_{config_data['plan_id']}_*.xlsx"),
            key=lambda f: f.stat().st_mtime,
            reverse=True
        )

        if verification_files:
            latest_file = verification_files[0]
            df = pd.read_excel(latest_file)
            st.session_state.verification_result = df
            st.session_state.verification_file = str(latest_file)
            add_log(f"✅ 参数验证完成！文件: {latest_file.name}")
            st.success("参数验证完成！")
        else:
            add_log("⚠️ 未找到验证文件", "ERROR")

    except Exception as e:
        add_log(f"❌ 验证失败: {str(e)}", "ERROR")
        st.error(f"验证失败: {str(e)}")


def execute_comprehensive(config_data: dict, config_manager):
    """
    执行综合分析

    Args:
        config_data: 配置数据字典
        config_manager: 配置管理器实例
    """
    st.session_state.execution_log = []
    add_log("开始综合分析...")

    try:
        sqltest = set_sqltest_config(config_data, config_manager)
        sqltest.fetch_data_and_export3()
        add_log("✅ 综合分析完成！")
        st.success("综合分析完成！")

    except Exception as e:
        add_log(f"❌ 执行失败: {str(e)}", "ERROR")
        st.error(f"执行失败: {str(e)}")


def execute_full_analysis(config_data: dict, config_manager):
    """
    执行完整分析

    Args:
        config_data: 配置数据字典
        config_manager: 配置管理器实例
    """
    st.session_state.execution_log = []
    add_log("开始完整分析...")

    try:
        sqltest = set_sqltest_config(config_data, config_manager)
        sqltest.fetch_all_results_and_export(config_data["plan_id"])
        add_log("✅ 完整分析完成！")
        st.success("完整分析完成！")

    except Exception as e:
        add_log(f"❌ 执行失败: {str(e)}", "ERROR")
        st.error(f"执行失败: {str(e)}")


def execute_basic_analysis(config_data: dict, config_manager):
    """
    执行基础分析

    Args:
        config_data: 配置数据字典
        config_manager: 配置管理器实例
    """
    st.session_state.execution_log = []
    add_log("开始基础分析...")

    try:
        sqltest = set_sqltest_config(config_data, config_manager)
        sqltest.fetch_data_and_export2()
        add_log("✅ 基础分析完成！")
        st.success("基础分析完成！")

    except Exception as e:
        add_log(f"❌ 执行失败: {str(e)}", "ERROR")
        st.error(f"执行失败: {str(e)}")


def show_results():
    """
    展示执行结果和下载链接
    """
    st.subheader("输出文件")

    # 获取 reports 目录
    reports_dir = project_root / "reports"
    if not reports_dir.exists():
        st.info("暂无输出文件")
        return

    # 获取所有 Excel 文件
    excel_files = sorted(reports_dir.glob("*.xlsx"), key=lambda f: f.stat().st_mtime, reverse=True)

    if not excel_files:
        st.info("暂无输出文件")
        return

    # 按文件类型分组展示
    verification_files = [f for f in excel_files if f.name.startswith("parameter_verification")]
    analysis_files = [f for f in excel_files if not f.name.startswith("parameter_verification")]

    # 展示最新15个文件（包含验证文件）
    all_files = (verification_files + analysis_files)[:15]

    st.markdown(f"**最近的输出文件（共 {len(all_files)} 个）：**")

    # 创建3列布局
    for i in range(0, len(all_files), 3):
        cols = st.columns(3)
        for j, col in enumerate(cols):
            if i + j < len(all_files):
                file_path = all_files[i + j]
                with col:
                    st.markdown(f"**{file_path.name}**")
                    st.caption(f"生成时间: {datetime.fromtimestamp(file_path.stat().st_mtime).strftime('%Y-%m-%d %H:%M:%S')}")
                    with open(file_path, "rb") as f:
                        st.download_button(
                            "📥 下载",
                            data=f.read(),
                            file_name=file_path.name,
                            key=f"download_{i}_{j}",
                            use_container_width=True,
                        )


# Streamlit 入口
if __name__ == "__main__":
    st.set_page_config(
        page_title="智能排餐参数验证工具",
        page_icon="🍽️",
        layout="wide",
    )

    main()
