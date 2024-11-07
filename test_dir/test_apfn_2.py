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

    def test_Afpn_1_1(self):
        """
        食材管理-食材分类
        """
        s = Steps().open(f"{BaseUrl}/ingredientManage/category")
        s.sleep(3)
        # 点击添加食材分类
        s.find("#app > section > section > main > div.scat-basic-layout-router-view_oRIA-eH6 > div > div.search-tree > div.scat-card_zy63xRVm.s-flex.s-flex-column.s-full > div.search-tree-top > button > span").click()
        s.sleep(2)
        # 输入分类名称
        s.find("body > div:nth-child(6) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > form > div > div > div.ant-col.ant-col-12.ant-form-item-control.css-12kx9o0 > div > div > div > span > #form_item_name").type("食材分类测试")
        # 点击确定按钮
        s.find("body > div:nth-child(6) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-footer > button.css-12kx9o0.ant-btn.ant-btn-primary > span").click()
        s.sleep(1)
        # 点击搜索测试分类
        s.find("#app > section > section > main > div.scat-basic-layout-router-view_oRIA-eH6 > div > div.search-tree > div.scat-card_zy63xRVm.s-flex.s-flex-column.s-full > div.search-tree-top > span > input").type("食材分类测试")
        s.sleep(1)
        # 选择搜索结果中的测试分类
        s.find("#app > section > section > main > div.scat-basic-layout-router-view_oRIA-eH6 > div > div.search-tree > div.scat-card_zy63xRVm.s-flex.s-flex-column.s-full > div.s-flex-1 > div > div > div > div.ant-tree-list > div.ant-tree-list-holder > div > div > div > span.ant-tree-node-content-wrapper.ant-tree-node-content-wrapper-normal > span > div > div:nth-child(1)").click()
        s.sleep(1)
        # 点击输入框，进行编辑
        s.find("#form_item_name").clear().type("食材分类测试1")
        # 点击保存
        s.find("#app > section > section > main > div.scat-basic-layout-router-view_oRIA-eH6 > div > div.scat-card_zy63xRVm.form > div > div.form-content.s-flex-1 > div > div > form > div:nth-child(2) > div > div.ant-col.ant-form-item-control.css-12kx9o0 > div > div > button:nth-child(2) > span").click()
        s.sleep(1)
        self.assertText("编辑成功")
        # 点击删除按钮
        s.find("#app > section > section > main > div.scat-basic-layout-router-view_oRIA-eH6 > div > div.scat-card_zy63xRVm.form > div > div.form-content.s-flex-1 > div > div > form > div:nth-child(2) > div > div.ant-col.ant-form-item-control.css-12kx9o0 > div > div > button.css-12kx9o0.ant-btn.ant-btn-primary.ant-btn-background-ghost.ant-btn-dangerous.scat-button_gxH2v2M8 > span").click()
        s.sleep(1)
        # 二次确认删除
        s.find("body > div:nth-child(7) > div > div.ant-modal-wrap > div > div.ant-modal-content > div > div > div.ant-modal-confirm-btns > button.css-12kx9o0.ant-btn.ant-btn-primary > span").click()
        s.sleep(1)
        self.assertText("删除成功")


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
        # 选择食材分类中的第一个选项  使用debugger方式 查看选中的元素
        s.find("#app > section > section > main > div.scat-basic-layout-router-view_oRIA-eH6 > div.content > div > div > form > div > div > div.ant-row.css-12kx9o0 > div:nth-child(4) > div > div > div.ant-col.ant-form-item-control.css-12kx9o0 > div > div > div > div:nth-child(3) > div > div > div > div > div > div.ant-select-tree-list > div.ant-select-tree-list-holder > div > div > div:nth-child(6) > span.ant-select-tree-switcher.ant-select-tree-switcher_close > span").click()
        s.sleep(1)
        s.find("#app > section > section > main > div.scat-basic-layout-router-view_oRIA-eH6 > div.content > div > div > form > div > div > div.ant-row.css-12kx9o0 > div:nth-child(4) > div > div > div.ant-col.ant-form-item-control.css-12kx9o0 > div > div > div > div:nth-child(3) > div > div > div > div > div > div.ant-select-tree-list > div.ant-select-tree-list-holder > div > div > div:nth-child(9)").click()
        s.sleep(1)
        # 选择食材类型 主料
        s.find("#app > section > section > main > div.scat-basic-layout-router-view_oRIA-eH6 > div.content > div > div > form > div > div > div.ant-row.css-12kx9o0 > div:nth-child(5) > div > div > div.ant-col.ant-form-item-control.css-12kx9o0 > div > div > div").click()
        s.sleep(1)
        s.find("#app > section > section > main > div.scat-basic-layout-router-view_oRIA-eH6 > div.content > div > div > form > div > div > div.ant-row.css-12kx9o0 > div:nth-child(5) > div > div > div.ant-col.ant-form-item-control.css-12kx9o0 > div > div > div > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div:nth-child(1)").click()
        s.sleep(1)
        # 输入标准净菜率
        s.find("#app > section > section > main > div.scat-basic-layout-router-view_oRIA-eH6 > div.content > div > div > form > div > div > div.ant-row.css-12kx9o0 > div:nth-child(6) > div > div > div.ant-col.ant-form-item-control.css-12kx9o0 > div > div > div > div > div > div.ant-input-number.ant-input-number-in-form-item.scat-input-number_XsjRs88q.scat-input-number-hide-addon-after_hFd-cJUG.css-12kx9o0 > div > input").type("98.5")
        s.sleep(1)
        # 输入备注
        s.find("#form_item_remark").type("测试备注")
        s.sleep(1)
        # 点击保存按钮
        s.find("#app > section > section > main > div.scat-basic-layout-router-view_oRIA-eH6 > div.scat-fixed-filter_xxtavGtw > div.s-nowrap.s-flex-nowrap > button.css-12kx9o0.ant-btn.ant-btn-primary.scat-button_gxH2v2M8 > span").click()
        s.sleep(1)
        self.assertText("添加成功")
        # 点击删除按钮，并二次确定删除
        s.find("#app > section > section > main > div.scat-basic-layout-router-view_oRIA-eH6 > div:nth-child(2) > div > div > div > div > div > div > table > tbody > tr:nth-child(2) > td.ant-table-cell.ant-table-cell-fix-right.ant-table-cell-fix-right-first > button.css-12kx9o0.ant-btn.ant-btn-link.ant-btn-dangerous > span").click()
        s.sleep(1)
        s.find("body > div:nth-child(6) > div > div > div > div.ant-popover-inner > div > div > div.ant-popconfirm-buttons > button.css-12kx9o0.ant-btn.ant-btn-primary.ant-btn-sm.ant-btn-dangerous > span").click()
        s.sleep(1)
        self.assertText("删除成功")


    def test_Afpn_2_1(self):
        """
        菜谱管理-菜谱分类
        """
        s = Steps().open(f"{BaseUrl}/recipeManage/category")
        s.sleep(1)
        # 点击添加分类按钮
        s.find("#app > section > section > main > div.scat-basic-layout-router-view_oRIA-eH6 > div > div.search-tree > div.scat-card_zy63xRVm.s-flex.s-flex-column.s-full > div.search-tree-top > button > span").click()
        s.sleep(1)
        # 输入分类名称
        s.find("body > div:nth-child(6) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > form > div > div > div.ant-col.ant-col-12.ant-form-item-control.css-12kx9o0 > div > div > div > span > #form_item_name").type("菜谱分类测试")
        s.find("body > div:nth-child(6) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-footer > button.css-12kx9o0.ant-btn.ant-btn-primary > span").click()
        s.sleep(1)
        self.assertText("添加成功")
        # 输入分类名称搜索后，点击搜索出的内容
        s.find("#app > section > section > main > div.scat-basic-layout-router-view_oRIA-eH6 > div > div.search-tree > div.scat-card_zy63xRVm.s-flex.s-flex-column.s-full > div.search-tree-top > span > input").type("菜谱分类测试")
        s.sleep(1)
        s.find("#app > section > section > main > div.scat-basic-layout-router-view_oRIA-eH6 > div > div.search-tree > div.scat-card_zy63xRVm.s-flex.s-flex-column.s-full > div.s-flex-1 > div > div > div > div.ant-tree-list > div.ant-tree-list-holder > div > div > div > span.ant-tree-node-content-wrapper.ant-tree-node-content-wrapper-normal > span > div > div:nth-child(1)").click()
        s.sleep(1)
        # 点击输入框，进行编辑
        s.find("#form_item_name").clear().type("菜谱分类测试1")
        # 点击保存
        s.find("#app > section > section > main > div.scat-basic-layout-router-view_oRIA-eH6 > div > div.scat-card_zy63xRVm.form > div > div.form-content.s-flex-1 > div > div > form > div:nth-child(2) > div > div.ant-col.ant-form-item-control.css-12kx9o0 > div > div > button:nth-child(2) > span").click()
        s.sleep(1)
        self.assertText("编辑成功")
        # 点击删除按钮，并二次确认删除
        s.find("#app > section > section > main > div.scat-basic-layout-router-view_oRIA-eH6 > div > div.scat-card_zy63xRVm.form > div > div.form-content.s-flex-1 > div > div > form > div:nth-child(2) > div > div.ant-col.ant-form-item-control.css-12kx9o0 > div > div > button.css-12kx9o0.ant-btn.ant-btn-primary.ant-btn-background-ghost.ant-btn-dangerous.scat-button_gxH2v2M8 > span").click()
        s.sleep(1)
        s.find("body > div:nth-child(7) > div > div.ant-modal-wrap > div > div.ant-modal-content > div > div > div.ant-modal-confirm-btns > button.css-12kx9o0.ant-btn.ant-btn-primary > span").click()
        s.sleep(1)
        self.assertText("删除成功")


    def test_Afpn_2_2(self):
        """
        菜谱管理-菜谱列表
        """
        s = Steps().open(f"{BaseUrl}/recipeManage/list")
        s.sleep(1)
        # 选择类型 自研
        s.find("#rc_select_1").click()
        s.sleep(1)
        s.find("#app > section > section > main > div.scat-basic-layout-router-view_oRIA-eH6 > div > div.scat-card_zy63xRVm.content > form > div > div:nth-child(4) > div > div > div.ant-col.ant-form-item-control.css-12kx9o0 > div > div > div > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div:nth-child(1)").click()
        s.sleep(1)
        # 选择排餐大类 第一个
        s.find("#rc_select_2").click()
        s.sleep(1)
        s.find("#app > section > section > main > div.scat-basic-layout-router-view_oRIA-eH6 > div > div.scat-card_zy63xRVm.content > form > div > div:nth-child(5) > div > div > div.ant-col.ant-form-item-control.css-12kx9o0 > div > div > div > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div:nth-child(1)").click()
        # s.find("#app > section > section > main > div.scat-basic-layout-router-view_oRIA-eH6 > div > div.scat-card_zy63xRVm.content > form > div > div:nth-child(5) > div > div > div.ant-col.ant-form-item-control.css-12kx9o0 > div > div > div > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div > div:contains('川菜')").click()
        s.sleep(1)
        # 选择排餐小类 第一个
        s.find("#rc_select_3").click()
        s.sleep(1)
        s.find("#app > section > section > main > div.scat-basic-layout-router-view_oRIA-eH6 > div > div.scat-card_zy63xRVm.content > form > div > div:nth-child(6) > div > div > div.ant-col.ant-form-item-control.css-12kx9o0 > div > div > div > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div:nth-child(1)").click()
        # s.find("#app > section > section > main > div.scat-basic-layout-router-view_oRIA-eH6 > div > div.scat-card_zy63xRVm.content > form > div > div:nth-child(6) > div > div > div.ant-col.ant-form-item-control.css-12kx9o0 > div > div > div > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div[text='麻辣']").click()
        s.sleep(1)
        # 点击新增菜谱
        s.find("#app > section > section > main > div.scat-basic-layout-router-view_oRIA-eH6 > div > div.scat-card_zy63xRVm.content > form > div > div.ant-col.ant-col-xs-24.ant-col-sm-24.ant-col-md-12.ant-col-lg-16.ant-col-xl-16.ant-col-xxl-6.scat-search-col_WKLC9-JI.css-12kx9o0 > div > div > div > div > div > button:nth-child(2)").click()
        s.sleep(1)
        # 刷新页面 确保后面的元素标值位正确计算
        s.refresh()
        # 输入菜谱编码
        s.find("#form_item_code").type("ceshitzk123")
        # 输入菜谱名称
        s.find("#form_item_name").type("测试菜谱tzk")
        # 选择菜谱分类
        s.find("#form_item_categoryId").click()
        s.sleep(1)
        s.find("#app > section > section > main > div.scat-basic-layout-router-view_oRIA-eH6 > div.content > div > div > form > div:nth-child(1) > div > div.ant-row.css-12kx9o0 > div:nth-child(3) > div > div > div.ant-col.ant-form-item-control.css-12kx9o0 > div > div > div > div:nth-child(3) > div > div > div > div > div > div.ant-select-tree-list > div.ant-select-tree-list-holder > div > div > div:nth-child(2)").click()
        # 选择使用范围
        s.find("#rc_select_1").click()
        s.sleep(1)
        s.find("#app > section > section > main > div.scat-basic-layout-router-view_oRIA-eH6 > div.content > div > div > form > div:nth-child(1) > div > div.ant-row.css-12kx9o0 > div:nth-child(4) > div > div > div.ant-col.ant-form-item-control.css-12kx9o0 > div > div > div > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div:nth-child(1)").click()
        # 输入备注
        s.find("#form_item_remark").type("测试备注")
        # 选择排餐大类
        s.find("#rc_select_2").click()
        s.sleep(1)
        s.find("#app > section > section > main > div.scat-basic-layout-router-view_oRIA-eH6 > div.content > div > div > form > div:nth-child(2) > div > div:nth-child(2) > div:nth-child(1) > div > div > div.ant-col.ant-form-item-control.css-12kx9o0 > div > div > div > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div:nth-child(1)").click()
        # 选择排餐小类
        s.find("#rc_select_3").click()
        s.sleep(1)
        s.find("#app > section > section > main > div.scat-basic-layout-router-view_oRIA-eH6 > div.content > div > div > form > div:nth-child(2) > div > div:nth-child(2) > div:nth-child(2) > div > div > div.ant-col.ant-form-item-control.css-12kx9o0 > div > div > div > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div:nth-child(1)").click()
        # 添加标签
        s.find("#app > section > section > main > div.scat-basic-layout-router-view_oRIA-eH6 > div.content > div > div > form > div:nth-child(2) > div > div:nth-child(3) > div > div > div > div.ant-col.ant-form-item-label.css-12kx9o0 > label > span > div > span > div").click()
        s.sleep(1)
        s.find("body > div:nth-child(6) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div:nth-child(1)").click()
        # 点击保存
        s.find("#app > section > section > main > div.scat-basic-layout-router-view_oRIA-eH6 > div.scat-fixed-filter_xxtavGtw > div.s-nowrap.s-flex-nowrap > button.css-12kx9o0.ant-btn.ant-btn-primary.scat-button_gxH2v2M8").click()
        s.sleep(1)
        self.assertText("添加成功")
        # 删除
        s.find("#app > section > section > main > div.scat-basic-layout-router-view_oRIA-eH6 > div > div.scat-card_zy63xRVm.content > div > div > div > div > div > div > table > tbody > tr:nth-child(2) > td.ant-table-cell.ant-table-cell-fix-right.ant-table-cell-fix-right-first > button.css-12kx9o0.ant-btn.ant-btn-link.ant-btn-dangerous > span").click()
        s.sleep(1)
        s.find("body > div:nth-child(6) > div > div > div > div.ant-popover-inner > div > div > div.ant-popconfirm-buttons > button.css-12kx9o0.ant-btn.ant-btn-primary.ant-btn-sm.ant-btn-dangerous > span").click()
        s.sleep(1)
        self.assertText("删除成功")


    def test_Afpn_2_3(self):
        """
        菜谱管理-排餐配置
        """
        s = Steps().open(f"{BaseUrl}/recipeManage/arrange")
        s.sleep(2)
        # 新增排餐分类
        s.find("#rc-tabs-0-panel-category > div > div > form > div > div:nth-child(2) > div > div > div > div > div > button:nth-child(2)").click()
        s.sleep(1)
        # 输入分类名称
        s.find("#form_item_name").type("测试分类")
        # 点击保存
        s.find("body > div:nth-child(5) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-footer > button.css-12kx9o0.ant-btn.ant-btn-primary > span").click()
        s.sleep(1)
        self.assertText("添加成功")
        # 输入名称搜索
        s.find("#rc-tabs-0-panel-category > div > div > form > div > div:nth-child(1) > div > div > div.ant-col.ant-form-item-control.css-12kx9o0 > div > div > span > input").type("测试分类")
        s.sleep(1)
        # 删除
        s.find("#rc-tabs-0-panel-category > div > div > div > div > div > div > div > div > table > tbody > tr.ant-table-row.ant-table-row-level-0 > td.ant-table-cell.ant-table-cell-fix-right.ant-table-cell-fix-right-first > button.css-12kx9o0.ant-btn.ant-btn-link.ant-btn-dangerous > span").click()
        s.sleep(1)
        s.find("body > div:nth-child(6) > div > div > div > div.ant-popover-inner > div > div > div.ant-popconfirm-buttons > button.css-12kx9o0.ant-btn.ant-btn-primary.ant-btn-sm.ant-btn-dangerous > span").click()
        s.sleep(1)
        self.assertText("删除成功")
        # 刷新页面，切换到排餐标签
        s.refresh()
        s.sleep(1)
        s.find("#rc-tabs-0-tab-label").click()
        s.sleep(1)
        # 新增排餐标签
        s.find("#rc-tabs-0-panel-label > div > div > form > div > div:nth-child(2) > div > div > div > div > div > button:nth-child(2) > span").click()
        s.sleep(1)
        # 输入标签名称
        s.find("#form_item_name").type("测试标签")
        # 点击保存
        s.find("body > div:nth-child(5) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-footer > button.css-12kx9o0.ant-btn.ant-btn-primary > span").click()
        s.sleep(1)
        self.assertText("添加成功")
        # 输入名称搜索
        s.find("#rc-tabs-0-panel-label > div > div > form > div > div:nth-child(1) > div > div > div.ant-col.ant-form-item-control.css-12kx9o0 > div > div > span > input").type("测试标签")
        s.sleep(1)
        # 删除
        s.find("#rc-tabs-0-panel-label > div > div > div > div > div > div > div > div > table > tbody > tr.ant-table-row.ant-table-row-level-0 > td.ant-table-cell.ant-table-cell-fix-right.ant-table-cell-fix-right-first > button.css-12kx9o0.ant-btn.ant-btn-link.ant-btn-dangerous > span").click()
        s.sleep(1)
        s.find("body > div:nth-child(6) > div > div > div > div.ant-popover-inner > div > div > div.ant-popconfirm-buttons > button.css-12kx9o0.ant-btn.ant-btn-primary.ant-btn-sm.ant-btn-dangerous > span").click()
        s.sleep(1)
        self.assertText("删除成功")



    def test_Afpn_3_1(self):
        """
        菜谱授权-菜谱分组
        """
        s = Steps().open(f"{BaseUrl}/recipeAuth/recipeGroup")
        s.sleep(1)
        # 新增
        s.find("#app > section > section > main > div.scat-basic-layout-router-view_oRIA-eH6 > div.scat-card_zy63xRVm.s-m-b-16 > form > div > div:nth-child(2) > div > div > div > div > div > button:nth-child(2) > span").click()
        s.sleep(1)
        # 输入菜谱分组名称
        s.find("#form_item_name").type("测试分组")
        # 输入备注
        s.find("#form_item_remark").type("测试备注")
        # 添加菜谱
        s.find("#app > section > section > main > div.scat-basic-layout-router-view_oRIA-eH6 > div.content > div > div > form > div:nth-child(2) > div > div.s-flex-yox-center.s-flex-x-between > div.s-gap-5-10.s-flex-x-right.s-m-l-10.title-right_EpHF-9kF > div > button > span").click()
        s.sleep(1)
        # 选择第一次菜谱
        s.find("body > div:nth-child(6) > div > div.ant-modal-wrap.ant-modal-centered > div > div.ant-modal-content > div.ant-modal-body > div.s-gap-16.s-flex-nowrap.s-w-full > div:nth-child(2) > div > div > div > div > div > div > table > tbody > tr:nth-child(2) > td.ant-table-cell.ant-table-cell-fix-left.ant-table-cell-fix-left-last.ant-table-selection-column > label > span > input").click()
        s.sleep(1)
        # 确定
        s.find("body > div:nth-child(6) > div > div.ant-modal-wrap.ant-modal-centered > div > div.ant-modal-content > div.ant-modal-footer > button.css-12kx9o0.ant-btn.ant-btn-primary > span").click()
        s.sleep(1)
        # 点击保存
        s.find("#app > section > section > main > div.scat-basic-layout-router-view_oRIA-eH6 > div.scat-fixed-filter_xxtavGtw > div.s-nowrap.s-flex-nowrap > button.css-12kx9o0.ant-btn.ant-btn-primary.scat-button_gxH2v2M8 > span").click()
        s.sleep(1)
        self.assertText("添加成功")
        # 输入名称搜索
        s.find("#app > section > section > main > div.scat-basic-layout-router-view_oRIA-eH6 > div.scat-card_zy63xRVm.s-m-b-16 > form > div > div:nth-child(1) > div > div > div.ant-col.ant-form-item-control.css-12kx9o0 > div > div > span > input").type("测试分组")
        s.sleep(1)
        # 删除
        s.find("#app > section > section > main > div.scat-basic-layout-router-view_oRIA-eH6 > div:nth-child(2) > div > div > div > div > div > div > table > tbody > tr.ant-table-row.ant-table-row-level-0 > td.ant-table-cell.ant-table-cell-fix-right.ant-table-cell-fix-right-first > button.css-12kx9o0.ant-btn.ant-btn-link.ant-btn-dangerous > span").click()
        s.sleep(1)
        s.find("body > div:nth-child(6) > div > div > div > div.ant-popover-inner > div > div > div.ant-popconfirm-buttons > button.css-12kx9o0.ant-btn.ant-btn-primary.ant-btn-sm.ant-btn-dangerous > span").click()
        s.sleep(1)
        self.assertText("删除成功")


    def test_Afpn_3_2(self):
        """
        菜谱授权-授权管理
        """
        s = Steps().open(f"{BaseUrl}/recipeAuth/authorization")
        s.sleep(1)
        # 被授权组织筛选
        s.find("#rc_select_0").click()
        s.sleep(1)
        # 选择组织
        s.find("#app > section > section > main > div.scat-basic-layout-router-view_oRIA-eH6 > div.scat-card_zy63xRVm.s-m-b-16 > form > div > div.ant-col.ant-col-xs-24.ant-col-sm-12.ant-col-md-8.ant-col-lg-8.ant-col-xl-6.ant-col-xxl-4.scat-search-col_WKLC9-JI.css-12kx9o0 > div > div > div.ant-col.ant-form-item-control.css-12kx9o0 > div > div > div > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div:nth-child(1)").click()
        s.sleep(1)
        # 选择组织授权
        s.find("#app > section > section > main > div.scat-basic-layout-router-view_oRIA-eH6 > div.scat-card_zy63xRVm.s-m-b-16 > form > div > div.ant-col.ant-col-xs-24.ant-col-sm-24.ant-col-md-16.ant-col-lg-16.ant-col-xl-12.ant-col-xxl-8.scat-search-col_WKLC9-JI.css-12kx9o0 > div > div > div > div > div > button:nth-child(3) > span").click()
        s.sleep(1)
        # 选择菜谱分组，第一个
        s.refresh()
        s.find("#rc_select_0").click()
        s.sleep(1)
        s.find("#app > section > section > main > div.scat-basic-layout-router-view_oRIA-eH6 > div.scat-card_zy63xRVm > form > div > div:nth-child(1) > div > div.ant-col.ant-col-12.ant-form-item-control.css-12kx9o0 > div > div > div > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div:nth-child(1)").click()
        # 选择第一个菜谱分组
        s.find("#form_item_groupIdSet > div:nth-child(1) > div.ant-transfer-list-body.ant-transfer-list-body-with-search > ul > li:nth-child(1) > label > span > input").click()
        s.sleep(1)
        s.find("#form_item_groupIdSet > div.ant-transfer-operation > button:nth-child(1) > span > svg").click()
        # 点击保存
        s.find("#app > section > section > main > div.scat-basic-layout-router-view_oRIA-eH6 > div.scat-fixed-filter_xxtavGtw > div.s-nowrap.s-flex-nowrap > button.css-12kx9o0.ant-btn.ant-btn-primary.scat-button_gxH2v2M8 > span").click()
        s.sleep(1)
        self.assertText("添加成功")
        # 删除
        s.find("#app > section > section > main > div.scat-basic-layout-router-view_oRIA-eH6 > div:nth-child(2) > div > div > div > div > div > div > table > tbody > tr:nth-child(2) > td:nth-child(5) > button > span").click()
        s.sleep(1)
        s.find("body > div:nth-child(5) > div > div > div > div.ant-popover-inner > div > div > div.ant-popconfirm-buttons > button.css-12kx9o0.ant-btn.ant-btn-primary.ant-btn-sm.ant-btn-dangerous > span").click()
        s.sleep(1)
        self.assertText("删除成功")


        
    def test_Afpn_3_3(self):
        """
        菜谱授权-授权查询
        """
        s = Steps().open(f"{BaseUrl}/recipeAuth/query")
        s.sleep(1)
        # 被授权组织筛选
        s.find("#rc_select_0").click()
        s.sleep(1)
        # 选择组织
        s.find("#app > section > section > main > div.scat-basic-layout-router-view_oRIA-eH6 > div.scat-card_zy63xRVm.s-m-b-16 > form > div > div:nth-child(1) > div > div > div.ant-col.ant-form-item-control.css-12kx9o0 > div > div > div > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div:nth-child(1)").click()
        s.sleep(1)
        # 点击查询



if __name__ == '__main__':
    seldom.main(
                case='test_apfn_2.AfpnTest',
                browser="gc", 
                # browser="firefox",
                tester="tzk",
                description="菜谱",
                # debug=True
                )

