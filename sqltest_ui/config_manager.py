"""
配置方案管理器

负责保存、加载、删除配置方案，以及配置格式转换。
"""

import json
import logging
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)


class ConfigManager:
    """配置方案管理器"""

    def __init__(self, configs_dir: str):
        """
        初始化配置管理器

        Args:
            configs_dir: 配置文件存储目录
        """
        self.configs_dir = Path(configs_dir)
        self.configs_dir.mkdir(parents=True, exist_ok=True)

    def list_configs(self) -> list:
        """
        列出所有可用的配置方案名称

        Returns:
            配置方案名称列表（不含扩展名）
        """
        return [f.stem for f in self.configs_dir.glob("*.json")]

    def load_config(self, name: str) -> Optional[dict]:
        """
        加载指定名称的配置方案

        Args:
            name: 配置方案名称（不含扩展名）

        Returns:
            配置数据字典，不存在则返回None
        """
        config_file = self.configs_dir / f"{name}.json"
        if not config_file.exists():
            return None
        with open(config_file, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_config(self, name: str, config_data: dict) -> None:
        """
        保存配置方案

        Args:
            name: 配置方案名称（不含扩展名）
            config_data: 配置数据字典
        """
        config_file = self.configs_dir / f"{name}.json"
        with open(config_file, "w", encoding="utf-8") as f:
            json.dump(config_data, f, ensure_ascii=False, indent=4)
        logger.info(f"配置方案已保存: {config_file}")

    def delete_config(self, name: str) -> bool:
        """
        删除配置方案

        Args:
            name: 配置方案名称（不含扩展名）

        Returns:
            删除成功返回True，不存在返回False
        """
        config_file = self.configs_dir / f"{name}.json"
        if not config_file.exists():
            return False
        config_file.unlink()
        logger.info(f"配置方案已删除: {config_file}")
        return True

    def get_default_config(self) -> dict:
        """
        获取默认配置

        Returns:
            默认配置字典，若 default.json 不存在则返回内置默认值
        """
        default_config = self.load_config("default")
        if default_config:
            return default_config
        # 内置默认值
        return {
            "name": "默认配置",
            "plan_id": 25080403,
            "db": {
                "host": "10.50.11.77",
                "port": 3306,
                "user": "root",
                "password": "!@#$%^@2021@epfly",
                "database": "ifood_kitchen",
            },
            "consumption": {
                "std_weight": 350.0,
                "weight_tolerance": 0.02,
                "std_price": 24.0,
                "price_tolerance": 0.04,
            },
            "category": {
                "weight_ratio": {"大荤": 50, "小荤": 30, "素菜": 20},
                "dish_count": {"大荤": 8, "小荤": 7, "素菜": 4},
                "hot_dish_count": {"大荤": 2, "小荤": 2, "素菜": 1},
                "ratio_tolerance": 5.0,
            },
            "cook_method": {
                "ratio": {"炒菜机": 8, "蒸烤箱": 6, "人工": 5},
                "tolerance": 2.0,
            },
            "limits": {
                "non_hot_repeat_max_ratio": 20.0,
                "min_dish_weight": 50.0,
                "min_interval_days": 1,
            },
            "output": {
                "dir": r"d:\tangzk\py\seldom-web-testing\reports",
                "enable_timestamp": True,
            },
        }

    def config_to_sqltest_config(self, config_data: dict):
        """
        将配置字典转换为 sqltest.py 的 Config 对象

        Args:
            config_data: 配置数据字典

        Returns:
            sqltest.py 的 Config 实例
        """
        import sys
        from pathlib import Path as P

        # 确保 test_dir 在 Python 路径中
        project_root = P(__file__).parent.parent
        test_dir = project_root / "test_dir"
        if str(test_dir) not in sys.path:
            sys.path.insert(0, str(test_dir))

        from sqltest import Config

        return Config(
            DB_HOST=config_data.get("db", {}).get("host", "10.50.11.77"),
            DB_USER=config_data.get("db", {}).get("user", "root"),
            DB_PASSWORD=config_data.get("db", {}).get("password", ""),
            DB_NAME=config_data.get("db", {}).get("database", "ifood_kitchen"),
            DB_PORT=config_data.get("db", {}).get("port", 3306),
            PLAN_ID=config_data.get("plan_id", 25080403),
            STANDARD_WEIGHT=config_data.get("consumption", {}).get("std_weight", 350.0),
            WEIGHT_TOLERANCE=config_data.get("consumption", {}).get("weight_tolerance", 0.02),
            STANDARD_PRICE=config_data.get("consumption", {}).get("std_price", 24.0),
            PRICE_TOLERANCE=config_data.get("consumption", {}).get("price_tolerance", 0.04),
            CATEGORY_WEIGHT_RATIO=config_data.get("category", {}).get("weight_ratio", {"大荤": 50, "小荤": 30, "素菜": 20}),
            CATEGORY_DISH_COUNT=config_data.get("category", {}).get("dish_count", {"大荤": 8, "小荤": 7, "素菜": 4}),
            CATEGORY_HOT_DISH_COUNT=config_data.get("category", {}).get("hot_dish_count", {"大荤": 2, "小荤": 2, "素菜": 1}),
            CATEGORY_RATIO_TOLERANCE=config_data.get("category", {}).get("ratio_tolerance", 5.0),
            COOK_METHOD_RATIO=config_data.get("cook_method", {}).get("ratio", {"炒菜机": 8, "蒸烤箱": 6, "人工": 5}),
            COOK_METHOD_RATIO_TOLERANCE=config_data.get("cook_method", {}).get("tolerance", 2.0),
            NON_HOT_REPEAT_MAX_RATIO=config_data.get("limits", {}).get("non_hot_repeat_max_ratio", 20.0),
            MIN_DISH_WEIGHT=config_data.get("limits", {}).get("min_dish_weight", 50.0),
            MIN_INTERVAL_DAYS=config_data.get("limits", {}).get("min_interval_days", 1),
            OUTPUT_DIR=config_data.get("output", {}).get("dir", r"d:\tangzk\py\seldom-web-testing\reports"),
            ENABLE_TIMESTAMP=config_data.get("output", {}).get("enable_timestamp", True),
        )

    def sqltest_config_to_dict(self, config) -> dict:
        """
        将 sqltest.py 的 Config 对象转换为字典

        Args:
            config: sqltest.py 的 Config 实例

        Returns:
            配置数据字典
        """
        return {
            "name": "当前配置",
            "plan_id": config.PLAN_ID,
            "db": {
                "host": config.DB_HOST,
                "port": config.DB_PORT,
                "user": config.DB_USER,
                "password": config.DB_PASSWORD,
                "database": config.DB_NAME,
            },
            "consumption": {
                "std_weight": config.STANDARD_WEIGHT,
                "weight_tolerance": config.WEIGHT_TOLERANCE,
                "std_price": config.STANDARD_PRICE,
                "price_tolerance": config.PRICE_TOLERANCE,
            },
            "category": {
                "weight_ratio": dict(config.CATEGORY_WEIGHT_RATIO),
                "dish_count": dict(config.CATEGORY_DISH_COUNT),
                "hot_dish_count": dict(config.CATEGORY_HOT_DISH_COUNT),
                "ratio_tolerance": config.CATEGORY_RATIO_TOLERANCE,
            },
            "cook_method": {
                "ratio": dict(config.COOK_METHOD_RATIO),
                "tolerance": config.COOK_METHOD_RATIO_TOLERANCE,
            },
            "limits": {
                "non_hot_repeat_max_ratio": config.NON_HOT_REPEAT_MAX_RATIO,
                "min_dish_weight": config.MIN_DISH_WEIGHT,
                "min_interval_days": config.MIN_INTERVAL_DAYS,
            },
            "output": {
                "dir": config.OUTPUT_DIR,
                "enable_timestamp": config.ENABLE_TIMESTAMP,
            },
        }


# 便捷函数
def get_config_manager() -> ConfigManager:
    """获取全局配置管理器实例"""
    configs_dir = Path(__file__).parent / "configs"
    return ConfigManager(str(configs_dir))
