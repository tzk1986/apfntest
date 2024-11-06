import seldom
from seldom import Steps

# 测试环境 菜谱
BaseUrl = "http://10.50.11.120:9301"

# 预发布环境
# BaseUrl = "URL_ADDRESS"


class AfpnTest(seldom.TestCase):
    """
    菜谱
    """

    def start(self):

        print("开始测试")

    def end(self):
        print("结束测试")

    def test_Afpn_0_1(self):
        """
        登录
        """
        s = Steps().open(f"{BaseUrl}/login")
        # 输入用户名密码
        s.find("#form_item_phoneNumber").type("18930410999")
        s.find("#form_item_password").type("123456")
        s.find("#form_item_kaptchaCode").type("1")
        s.find("#app > div.scat-card_zy63xRVm.login-form > form > div.ant-form-item.css-12kx9o0.s-m-b-0 > div > div > div > div > button > span").click()

        s.sleep(3)
        self.get_cookies()
        print(self.get_cookies())

    # def test_Afpn_1_1(self):
    #     """
    #     食材管理-食材分类
    #     """
    #     s = Steps().open(f"{BaseUrl}/ingredientManage/category")
    #     s.sleep(3)
    #     # 点击添加食材分类
    #     s.find("#app > section > section > main > div.scat-basic-layout-router-view_oRIA-eH6 > div > div.search-tree > div.scat-card_zy63xRVm.s-flex.s-flex-column.s-full > div.search-tree-top > button > span").click()
    #     s.sleep(2)
    #     # 输入分类名称
    #     s.find("body > div:nth-child(6) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > form > div > div > div.ant-col.ant-col-12.ant-form-item-control.css-12kx9o0 > div > div > div > span > #form_item_name").type("测试分类")
    #     # 点击确定按钮
    #     s.find("body > div:nth-child(6) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-footer > button.css-12kx9o0.ant-btn.ant-btn-primary > span").click()
    #     s.sleep(1)
    #     # 点击搜索测试分类
    #     s.find("#app > section > section > main > div.scat-basic-layout-router-view_oRIA-eH6 > div > div.search-tree > div.scat-card_zy63xRVm.s-flex.s-flex-column.s-full > div.search-tree-top > span > input").type("测试分类")
    #     s.sleep(1)
    #     # 选择搜索结果中的测试分类
    #     s.find("#app > section > section > main > div.scat-basic-layout-router-view_oRIA-eH6 > div > div.search-tree > div.scat-card_zy63xRVm.s-flex.s-flex-column.s-full > div.s-flex-1 > div > div > div > div.ant-tree-list > div.ant-tree-list-holder > div > div > div > span.ant-tree-node-content-wrapper.ant-tree-node-content-wrapper-normal > span > div > div:nth-child(1)").click()
    #     s.sleep(1)
    #     # 点击输入框，进行编辑
    #     s.find("#form_item_name").clear().type("测试分类1")
    #     # 点击保存
    #     s.find("#app > section > section > main > div.scat-basic-layout-router-view_oRIA-eH6 > div > div.scat-card_zy63xRVm.form > div > div.form-content.s-flex-1 > div > div > form > div:nth-child(2) > div > div.ant-col.ant-form-item-control.css-12kx9o0 > div > div > button:nth-child(2) > span").click()
    #     s.sleep(1)
    #     self.assertText("编辑成功")
    #     # 点击删除按钮
    #     s.find("#app > section > section > main > div.scat-basic-layout-router-view_oRIA-eH6 > div > div.scat-card_zy63xRVm.form > div > div.form-content.s-flex-1 > div > div > form > div:nth-child(2) > div > div.ant-col.ant-form-item-control.css-12kx9o0 > div > div > button.css-12kx9o0.ant-btn.ant-btn-primary.ant-btn-background-ghost.ant-btn-dangerous.scat-button_gxH2v2M8 > span").click()
    #     s.sleep(1)
    #     # 二次确认删除
    #     s.find("body > div:nth-child(7) > div > div.ant-modal-wrap > div > div.ant-modal-content > div > div > div.ant-modal-confirm-btns > button.css-12kx9o0.ant-btn.ant-btn-primary > span").click()
    #     s.sleep(1)
    #     self.assertText("删除成功")



        pass

    def test_Afpn_1_2(self):
        """
        食材管理-食材列表
        """
        s = Steps().open(f"{BaseUrl}/ingredientManage/list")
        s.sleep(1)
        # 点击添加食材
        s.find("#app > section > section > main > div.scat-basic-layout-router-view_oRIA-eH6 > div.scat-card_zy63xRVm.s-m-b-16 > form > div > div:nth-child(6) > div > div > div > div > div > button:nth-child(2) > span").click()
        s.sleep(1)
        # 输入食材编码
        s.find("#app > section > section > main > div.scat-basic-layout-router-view_oRIA-eH6 > div.content > div > div > form > div > div > div.ant-row.css-12kx9o0 > div:nth-child(1) > div > div > div.ant-col.ant-form-item-control.css-12kx9o0 > div > div > span > input").type("test111")
        # 输入食材名称
        s.find("#app > section > section > main > div.scat-basic-layout-router-view_oRIA-eH6 > div.content > div > div > form > div > div > div.ant-row.css-12kx9o0 > div:nth-child(2) > div > div > div.ant-col.ant-form-item-control.css-12kx9o0 > div > div > span > input").type("测试食材")
        # 输入食材别名
        s.find("#app > section > section > main > div.scat-basic-layout-router-view_oRIA-eH6 > div.content > div > div > form > div > div > div.ant-row.css-12kx9o0 > div:nth-child(3) > div > div > div.ant-col.ant-form-item-control.css-12kx9o0 > div > div > span > input").type("后腿肉，火腿")
        # 选择食材分类
        s.find("#form_item_categoryId").click()
        s.sleep(1)
        # 选择食材分类中的第一个选项
        s.find(" ").click()


        pass

    # def test_Afpn_2_1(self):
    #     """
    #     菜谱管理-菜谱分类
    #     """
    #     s = Steps().open(f"{BaseUrl}/recipeManage/category")
    #     s.sleep(3)
    #     pass

    # def test_Afpn_2_2(self):
    #     """
    #     菜谱管理-菜谱列表
    #     """
    #     s = Steps().open(f"{BaseUrl}/recipeManage/list")
    #     s.sleep(3)
    #     pass

    # def test_Afpn_2_3(self):
    #     """
    #     菜谱管理-排餐配置
    #     """
    #     s = Steps().open(f"{BaseUrl}/recipeManage/arrange")
    #     s.sleep(3)
    #     pass

    # def test_Afpn_3_1(self):
    #     """
    #     菜谱授权-菜谱分组
    #     """
    #     s = Steps().open(f"{BaseUrl}/recipeAuth/recipeGroup")
    #     s.sleep(3)
    #     pass


    # def test_Afpn_3_2(self):
    #     """
    #     菜谱授权-授权管理
    #     """
    #     s = Steps().open(f"{BaseUrl}/recipeAuth/authorization")
    #     s.sleep(3)
    #     pass

        
    # def test_Afpn_3_3(self):
    #     """
    #     菜谱授权-授权查询
    #     """
    #     s = Steps().open(f"{BaseUrl}/recipeAuth/query")
    #     s.sleep(3)
    #     pass



if __name__ == '__main__':
    seldom.main(
                case='test_apfn_2.AfpnTest',
                browser="gc", 
                # browser="firefox",
                tester="tzk",
                description="菜谱",
                # debug=True
                )

