import seldom
from seldom import Steps


class BaiduTest(seldom.TestCase):

    def test_search_one(self):
        """
        百度搜索
        """
        s = Steps(url="http://www.baidu.com", desc="百度搜索")
        s.open().find("#kw").type("seldom").find("#su").click()
        self.assertInTitle("seldom")

        s.sleep(2)

    # def test_search_setting(self):
    #     """百度搜索设置"""
    #     s=Steps(url="http://www.baidu.com", desc="百度搜索设置")
    #     s.open().find("#s-usersetting-top").click()
    #     s.find("#s-user-setting-menu > div > a.setpref").click().sleep(2)
    #     s.find('[data-tabid="advanced"]').click().sleep(2)
    #     s.find("#q5_1").click().sleep(2)
    #     s.find('[data-tabid="general"]').click().sleep(2)
    #     s.find_text("保存设置").click()
    #     s.alert().accept()


if __name__ == '__main__':
    seldom.main(
                browser="gc", 
                # browser="firefox",
                tester="虫师", 
                debug=True
                )