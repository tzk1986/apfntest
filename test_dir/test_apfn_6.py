import seldom
from seldom import Steps
from selenium.webdriver import ChromeOptions
import requests


# 测试环境 供应商管理端 
BaseUrl = "http://supplieradmin.mall.com/"



# 预发布环境
# BaseUrl = ""

# 搜索商户
MerchantName = "艾佩"


class AfpnTest(seldom.TestCase):
    """
    供应商管理端
    """

    value = None

    def start(self):
        print("开始测试")

    def end(self):
        print("结束测试")

    def test_Afpn_001_1(self):
        """
        登录-站点管理
        """
        print(f"{BaseUrl}/login")
        s = Steps().open(f"{BaseUrl}/login")

        s.find("#form_item_username").type(
            "admin"
        )
        s.find("#form_item_password").type(
            "111111"
        )
        # 输入验证码
        s.find("#form_item_verifyCode").type(
            "1"
        )
        # 点击登录
        s.find("#app > div > div > div > div > div > button").click()
        s.sleep()
        self.get_cookies()
        print(self.get_cookies())
        s.open(f"{BaseUrl}/sysset_setting/site_info")
        s.sleep()
        s.sleep()
        
        

    # def test_Afpn_001_2(self):
    #     """
    #     菜谱授权管理-菜谱授权
    #     """
    #     s = Steps().open(f"{BaseUrl}#/menuGet")
    #     s.sleep()
    #     self.assertStatusOk()
        

    # def test_Afpn_002_1(self):
    #     """
    #     菜品管理-菜谱列表
    #     """
    #     s = Steps().open(f"{BaseUrl}/#/menuList/menuList")
    #     s.sleep()
    #     self.assertStatusOk()


    # def test_Afpn_002_2(self):
    #     """
    #     菜品管理-菜谱类型
    #     """
    #     s = Steps().open(f"{BaseUrl}/#/menuList/roleset")
    #     s.sleep()
    #     self.assertStatusOk()
        
        
    # def test_Afpn_002_3(self):
    #     """
    #     菜品管理-设备型号管理
    #     """
    #     s = Steps().open(f"{BaseUrl}/#/menuList/dictionary")
    #     s.sleep()
    #     self.assertStatusOk()
        

    # def test_Afpn_002_4(self):
    #     """
    #     菜品管理-原料管理
    #     """
    #     s = Steps().open(f"{BaseUrl}/#/menuList/systemlog")
    #     s.sleep()
    #     self.assertStatusOk()
        
        
    # def test_Afpn_002_5(self):
    #     """
    #     菜品管理-原料分类
    #     """
    #     s = Steps().open(f"{BaseUrl}/#/menuList/materialClassics")
    #     s.sleep()
    #     self.assertStatusOk()
        
        
    # def test_Afpn_003_1(self):
    #     """
    #     更新管理-APP更新
    #     """
    #     s = Steps().open(f"{BaseUrl}/#/update/appUpdate")
    #     s.sleep()
    #     self.assertStatusOk()
        
        
    # def test_Afpn_003_2(self):
    #     """
    #     更新管理-固件更新
    #     """
    #     s = Steps().open(f"{BaseUrl}/#/update/firmwareUpdate")
    #     s.sleep()
    #     self.assertStatusOk()
        

    # def test_Afpn_003_3(self):
    #     """
    #     更新管理-菜谱更新
    #     """
    #     s = Steps().open(f"{BaseUrl}/#/update/update")
    #     s.sleep()
    #     self.assertStatusOk()

    # def test_Afpn_004_1(self):
    #     """
    #     用户管理-用户信息管理
    #     """
    #     s = Steps().open(f"{BaseUrl}/#/user/userList")
    #     s.sleep()
    #     self.assertStatusOk()


    # def test_Afpn_004_2(self):
    #     """
    #     用户管理-企业架构管理
    #     """
    #     s = Steps().open(f"{BaseUrl}/#/user/userGroup")
    #     s.sleep()
    #     self.assertStatusOk()


    # def test_Afpn_005_1(self):
    #     """
    #     设备管理-设备信息管理
    #     """
    #     s = Steps().open(f"{BaseUrl}/#/device/deviceList")
    #     s.sleep()
    #     self.assertStatusOk()


    # def test_Afpn_005_2(self):
    #     """
    #     设备管理-设备分组管理
    #     """
    #     s = Steps().open(f"{BaseUrl}/#/device/deviceGroup")
    #     s.sleep()
    #     self.assertStatusOk()
    
    # def test_Afpn_005_3(self):
    #     """
    #     设备管理-远程通信
    #     """
    #     s = Steps().open(f"{BaseUrl}/#/device/mqtt")
    #     s.sleep()
    #     self.assertStatusOk()
    

    # def test_Afpn_006_1(self):
    #     """
    #     日志管理-全量日志
    #     """
    #     s = Steps().open(f"{BaseUrl}/#/log/logList")
    #     s.sleep()
    #     self.assertStatusOk()

    # def test_Afpn_006_2(self):
    #     """
    #     日志管理-每日烹饪
    #     """
    #     s = Steps().open(f"{BaseUrl}/#/log/cookList")
    #     s.sleep()
    #     self.assertStatusOk()
        
    # def test_Afpn_006_3(self):
    #     """
    #     日志管理-告警信息
    #     """
    #     s = Steps().open(f"{BaseUrl}/#/log/messageList")
    #     s.sleep()
    #     self.assertStatusOk()
        
    # def test_Afpn_006_4(self):
    #     """
    #     日志管理-位置信息
    #     """
    #     s = Steps().open(f"{BaseUrl}/#/log/location")
    #     s.sleep()
    #     self.assertStatusOk()        


# my_object = AfpnTest()  # 假设MyClass是一个类，my_object是它的一个实例
# attributes = dir(my_object)
# print(attributes)

# attributes = vars(my_object)
# print(attributes)

# instance_attributes = my_object.__dict__
# print(instance_attributes)


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
        case="test_apfn_6.AfpnTest",
        # browser=browser
        browser="gc",
        # browser="firefox",
        tester="tzk",
        description="供应商管理端",
        debug=True,
    )

