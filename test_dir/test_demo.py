import seldom
from seldom.utils import file
import seldom.webdriver
file.add_to_path(file.dir_dir)
from pages.po_page import AfpnPage, AfpnPage_2_1, AfpnPage_2_2, AfpnPage_3_1, AfpnPage_3_2, AfpnPage_4_1, AfpnPage_4_2, AfpnPage_4_3
from seldom import Steps



class AfpnTest(seldom.TestCase):
    """
    经营管理
    """
    def Login_test(self):
        """
        登录
        """
        s = Steps()
        s.open("http://10.50.11.120:9002/")\
        .find(AfpnPage.name_input)\
        .type("18335161013")\
        .find(AfpnPage.password_input)\
        .type("123456")\
        .find(AfpnPage.code_input)\
        .type("1")\
        .click(AfpnPage.login_button)
        # page = AfpnPage(print_log=True)
        
        self.assertInTitle("经营管理")

    # def test_Afpn_2_1(self):
    #     """
    #     入驻-总部
    #     """
    #     page = Steps().open("http://10.50.11.120:9002/").find(AfpnPage.name_input).type("18335161013").find(AfpnPage.password_input).type("123456").find(AfpnPage.code_input).type("1").click(AfpnPage.login_button)
    #     page = page.click('//*[@id="app"]/section/section/aside/div/div/div[2]/span')
    #     page = AfpnPage_2_1(print_log=True)
    #     page.search_input_1 = '1'
    #     page.search_button.click()
    #     self.sleep(2)




    

# class Basecase(seldom.TestCase):
#     """
#     基础测试类
#     """
#     @classmethod
#     def setUpClass(cls):
#         # 登录逻辑
#         cls.driver = seldom.webdriver(browser='chrome') # 使用seldom的DriverManager获取driver实例
#         cls.driver.get("http://10.50.11.120:9002/")
#         cls.driver.xpath('//*[@id="app"]/div/form/div[1]/div/div/input').send_keys("18335161013")
#         cls.driver.xpath('//*[@id="app"]/div/form/div[2]/div/div/input').send_keys("123456")
#         cls.driver.xpath('//*[@id="app"]/div/form/div[3]/div/div/div[1]/input').send_keys("1")
#         cls.driver.xpath('//*[@id="app"]/div/form/div[4]/div/button').click()

#     @classmethod
#     def tearDownClass(cls):
#         # 清理逻辑，例如退出登录或关闭浏览器
#         # 这里只是一个示例，你需要根据实际情况编写清理代码
#         pass  # 请根据实际情况填写清理代码

    
# class Loginpage(Page):
#     """登录 page"""
#     username = Element('//*[@id="app"]/div/form/div[1]/div/div/input')
#     password = Element('//*[@id="app"]/div/form/div[2]/div/div/input')
#     code_input = Element('//*[@id="app"]/div/form/div[3]/div/div/div[1]/input')
#     login_button = Element('//*[@id="app"]/div/form/div[4]/div/button')

#     def login(self, username="18335161013", password="123456"):
#         self.username.send_keys(username)
#         self.password.send_keys(password)
#         self.code_input.send_keys("1")
#         self.login_button.click()


# class BingTest(seldom.TestCase):
#     """
#     page object 设计模式
#     """

#     def test_Afpn_login(self):
#         """
#         A simple test
#         """
#         page = AfpnPage(print_log=True)
#         page.open("http://10.50.11.120:9002/")
#         page.name_input = "18335161013"
#         page.password_input = "112233"
#         page.code_input = "1"
#         page.login_button.click()
#         self.assertInTitle("经营管理")

# class AfpnTest(Basecase):
#     """
#     经营管理
#     """


#     def test_Afpn_2_1(self):
#         """
#         入驻-总部
#         """
#         page = AfpnPage_2_1(print_log=True)
#         """跳转到入驻页面"""
#         page.open("http://10.50.11.120:9002/storeEnter/settlein/head")

#         page.search_input_1 = "1"
#         page.search_button.click()
#         # page.open("URL_ADDRESS")
#         # page.name_input = "18335161013"
#         # page.password_input = "112233"
#         pass


if __name__ == '__main__':
    seldom.main(browser='chrome', 
                debug=True)