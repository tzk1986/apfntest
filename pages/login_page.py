import logging
from poium import Page, Element
from selenium import webdriver

logger = logging.getLogger(__name__)


class LoginPage(Page):
    # def __init__(self, driver: webdriver.Chrome, url):
    #     self.driver = driver
    #     self.root_uri = url
    username_loc = Element(xpath='//*[@id="app"]/div/form/div[1]/div/div/input')
    password_loc = Element(xpath='//*[@id="app"]/div/form/div[2]/div/div/input')
    code_loc = Element(xpath='//*[@id="app"]/div/form/div[3]/div/div/div[1]/input')
    click_loc = Element(xpath='//*[@id="app"]/div/form/div[4]/div/button')
    url = "http://10.50.11.120:9002/login"
    # zhuxiao_loc = Element(xpath='//*[@id="user-tools"]/a[3]')

    def login(self, username='18335161013', password='112233',code='1'):
        driver = webdriver.Chrome()

        page = LoginPage(driver)
        page.open(page.url)

        page.username_loc.send_keys(username)
        page.password_loc.send_keys(password)
        page.code_loc.send_keys(code)
        page.click_loc.click()
        return driver