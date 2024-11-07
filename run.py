import seldom
from selenium.webdriver import ChromeOptions

if __name__ == '__main__':
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--headless=new")  # 开启 headless 模式
    browser = {
        "browser": "chrome",
        "options": chrome_options
    }
    seldom.main(
        path="./test_dir/",
        browser=browser,  # 浏览器驱动
        # browser="gc", # google chrome
        # rerun=3,
        # debug=True,
    )
