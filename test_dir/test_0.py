import seldom
from seldom import Steps
from selenium.webdriver import ChromeOptions
import requests


# 测试环境 数字餐厅
BaseUrl = "http://10.50.11.120:9002"

BaseUrl_1 = "http://10.50.11.120:9001"

# 预发布环境
# BaseUrl = ""

# 搜索商户
MerchantName = "艾佩"


class AfpnTest(seldom.TestCase):
    """
    数字餐厅
    """

    value = None

    def start(self):
        print("开始测试")

    def end(self):
        print("结束测试")

    def test_Afpn_001_1(self):
        """
        登录
        """
        print(f"{BaseUrl}/login")
        s = Steps().open(f"{BaseUrl}/login")

        s.find("#app > div > div.login-box.s-h-center > form > div:nth-child(2) > div > div > input").type(
            "18335161013"
        )
        s.find("#app > div > div.login-box.s-h-center > form > div:nth-child(3) > div > div > input").type(
            "112233"
        )
        s.find(
            "#app > div > div.login-box.s-h-center > form > div:nth-child(4) > div > div > div.login-input-code.el-input.el-input--prefix > input"
        ).type("1")
        s.find("#app > div > div.login-box.s-h-center > form > div:nth-child(5) > div > button").click()
        s.sleep()
        self.get_cookies()
        print(self.get_cookies())
        s.open(f"{BaseUrl}/merchant/merchantList")
        s.sleep()
        # 商户简称搜索
        s.find(
            "#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div.search_option_left.s-gap-6-15 > div:nth-child(2) > div > input"
        ).type(f"{MerchantName}")
        s.sleep()
        # 选择跳转到餐厅
        s.find(
            "#app > section > section > section > main > section > section > main > div.main > div.table_content > div.el-table.el-table--fit.el-table--scrollable-x.el-table--enable-row-transition > div.el-table__fixed-right > div.el-table__fixed-body-wrapper > table > tbody > tr > td.el-table_1_column_7.el-table__cell > div > button:nth-child(4) > span"
        ).click()
        s.sleep(2)
        s.switch_to_window(1)
        self.get_cookies()
        print(self.get_cookies())
        
        
# 增加浏览器代理示例
if __name__ == "__main__":
    # proxy = "127.0.0.1:1080"  # 示例代理地址和端口

    # chrome_options = ChromeOptions()
    # chrome_options.add_argument(f"--proxy-server={proxy}")
    # browser = {
    #     "browser": "chrome",
    #     "options": chrome_options,
    # }
    seldom.main(
        case="test_0.AfpnTest",
        # browser=browser
        browser="gc",
        # browser="firefox",
        tester="tzk",
        description="数字餐厅",
        debug=True,
    )