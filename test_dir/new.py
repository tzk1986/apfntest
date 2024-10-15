import seldom
from seldom import Steps



class Test(seldom.TestCase):

    def test_key(self):

        Steps().open("https://www.baidu.com").find("#kw").type("seldom").find("#su").click()
        self.sleep(5)
        # self.open("https://www.baidu.com")

        # # 输入 seldomm
        # self.Keys(css="#kw").input("seldomm")

        # # 删除多输入的一个m
        # self.Keys(id_="kw").backspace()

        # # 输入“教程”
        # self.Keys(id_="kw").input("教程")

        # # ctrl+a 全选输入框内容
        # self.Keys(id_="kw").select_all()

        # # ctrl+x 剪切输入框内容
        # self.Keys(id_="kw").cut()

        # # ctrl+v 粘贴内容到输入框
        # self.Keys(id_="kw").paste()

        # # 通过回车键来代替单击操作
        # self.Keys(id_="kw").enter()
        
        # # 支持组合操作
        # self.Keys(id_="kw").select_all().cut()  # 全选剪切
        # self.Keys(id_="kw").select_all().delete()  # 全选删除


if __name__ == '__main__':
    seldom.main(browser="gc", debug=True)