import seldom
from seldom import Steps
import logging
from poium import Page, Element
from selenium import webdriver
# from pages.login_page import LoginPage

class LoginPage(Page):
    # def __init__(self, driver: webdriver.Chrome, url):
    #     self.driver = driver
    #     self.root_uri = url
    username_loc = Element(xpath='//*[@id="app"]/div/form/div[1]/div/div/input')
    password_loc = Element(xpath='//*[@id="app"]/div/form/div[2]/div/div/input')
    code_loc = Element(xpath='//*[@id="app"]/div/form/div[3]/div/div/div[1]/input')
    click_loc = Element(xpath='//*[@id="app"]/div/form/div[4]/div/button')
    url = "http://10.50.11.120:9002/login"


    def login(self, username='18335161013', password='112233',code='1'):
        driver = webdriver.Chrome()

        page = LoginPage(driver)
        page.open(page.url)

        page.username_loc.send_keys(username)
        page.password_loc.send_keys(password)
        page.code_loc.send_keys(code)
        page.click_loc.click()
        return driver

class AfpnTest_2(seldom.TestCase):

    def test_2_1(self):
        self.page = LoginPage.login(self)
        self.page.open("http://10.50.11.120:9002/storeEnter/settlein/head")

        self.assertText("入驻-总部")
        # s.find("#app > section > section > aside > div > div > div:nth-child(2) > span").click()
        




if __name__ == '__main__':
    seldom.main(browser="gc", tester="tzk",debug=True)