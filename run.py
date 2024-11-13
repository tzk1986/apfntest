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
        path=["./test_dir/test_apfn_1.py","./test_dir/test_apfn_2.py","./test_dir/test_apfn_3.py"],
        # case= "test_dir.test_apfn_1",
        browser=browser,  # 浏览器驱动
        # browser="gc", # google chrome
        # rerun=3,
        # debug=True,
        tester="tzk"
    )
