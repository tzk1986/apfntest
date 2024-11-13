import seldom
from seldom import Steps
from seldom import testdata
from selenium.webdriver import ChromeOptions

# 测试环境 采购
BaseUrl = "http://10.50.11.120:9005"
# 账号 18930410921 密码 123456

# 预发布环境
# BaseUrl = "URL_ADDRESS"

class AfpnTest(seldom.TestCase):
    """
    采购
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
        s.find("#form_item_phoneNumber").type("18930410921")
        s.find("#form_item_password").type("123456")
        s.find("#form_item_kaptchaCode").type("1")
        s.find("#app > div > form > div.ant-form-item.css-jmkaz5.s-m-b-0 > div > div > div > div > button > span").click()

        s.sleep(3)
        self.get_cookies()
        print(self.get_cookies())

    def test_Afpn_1_1(self):
        """
        基础数据-计量单位
        """
        s = Steps()
        s.open(f"{BaseUrl}/basicData/measureUnit")
        s.sleep(1)
        # 选择单位类型的第一个
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div:nth-child(1) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div:nth-child(1) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div:nth-child(1)").click()
        s.sleep(1)
        # 输入单位名称
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div:nth-child(2) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > span > input").type("test")
        s.sleep(1)
        # 点击新增
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div:nth-child(3) > div > div > div > div > div > button:nth-child(2) > span").click()
        s.sleep(1)
        # 单位类型选择新增
        s.find("#form_item_unitType").click()
        s.sleep(1)
        s.find("body > div:nth-child(5) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > form > div:nth-child(1) > div > div.ant-col.ant-col-12.ant-form-item-control.css-jmkaz5 > div > div > div > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div:nth-child(1)").click()
        s.sleep(1)
        # 输入单位名称
        s.find("#form_item_unitName").type("test")
        # 点击确定
        s.find("body > div:nth-child(5) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-footer > button.css-jmkaz5.ant-btn.ant-btn-primary > span").click()
        s.sleep(1)
        # 点击删除
        s.find("#app > section > section > main > div:nth-child(2) > div:nth-child(2) > div > div > div > div > div > div > table > tbody > tr.ant-table-row.ant-table-row-level-0 > td.ant-table-cell.ant-table-cell-fix-right.ant-table-cell-fix-right-first > button:nth-child(2) > span").click()
        s.sleep(1)
        # 二次确认
        s.find("body > div:nth-child(6) > div > div > div > div.ant-popover-inner > div > div > div.ant-popconfirm-buttons > button.css-jmkaz5.ant-btn.ant-btn-primary.ant-btn-sm.ant-btn-dangerous > span").click()
        s.sleep(1)
        self.assertText("删除成功")


    def test_Afpn_1_2(self):
        """
        基础数据-供应商
        """
        s = Steps()
        s.open(f"{BaseUrl}/basicData/supplierList")
        s.sleep(1)
        # 选择状态 待入驻 启用 禁用
        s.find("#rc_select_0").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div:nth-child(3) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div:nth-child(2)").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div:nth-child(3) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div.ant-select-selector").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div:nth-child(3) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div:nth-child(3)").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div:nth-child(3) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div.ant-select-selector").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div:nth-child(3) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div:nth-child(1)").click()
        s.sleep(1)
        # 点击新增
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div:nth-child(4) > div > div > div > div > div > button:nth-child(2) > span").click()
        s.sleep(1)
        # 输入供应商名称
        s.find("#form_item_supplierName").type("test")
        # 输入纳税人登记号
        s.find("#form_item_taxNo").type(testdata.get_digits(9))
        # 输入法人
        s.find("#form_item_legalPerson").type(testdata.username(language="zh"))
        # 输入业务联系人
        s.find("#form_item_contactPerson").type(testdata.username(language="zh"))
        # 输入业务联系人电话
        s.find("#form_item_contactPhone").type(testdata.get_phone())
        # 输入企业地址
        s.find("#form_item_address").type("测试地址")
        # 输入注册资金
        s.find("#form_item_registeredCapital").type(testdata.get_digits(6))
        # 输入邮箱
        s.find("#form_item_email").type(testdata.get_email())
        # 选择供应商范围 选择不限
        s.find("#form_item_supplyScopeType > label:nth-child(1) > span.ant-radio > input").click()
        # 输入备注
        s.find("#form_item_remark").type("测试备注")
        # 选择供应商类别
        s.find("#app > section > section > main > div:nth-child(2) > div > div > form > div.SCard-module__s-card___jVkOR > div > div:nth-child(13) > div > div > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div.ant-select-selector > div").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div > div > form > div.SCard-module__s-card___jVkOR > div > div:nth-child(13) > div > div > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div:nth-child(2) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div:nth-child(1)").click()
        s.sleep(1)
        # 点击提交
        s.find("#app > section > section > main > div:nth-child(2) > div > div > form > div.ant-form-item.css-jmkaz5.s-m-t-50 > div > div > div > div > div > button.css-jmkaz5.ant-btn.ant-btn-primary.SButton-module__s-button___IkZHy > span").click()
        s.sleep(1)
        self.assertText("供应商名称不能重复")   


    def test_Afpn_1_3(self):
        """
        基础数据-商户配置
        """
        s = Steps()
        s.open(f"{BaseUrl}/basicData/merchant")
        s.sleep(1)
        # 选择自定义
        s.find("#form_item_settlementCollectCycle > label:nth-child(2) > span.ant-radio > input").click()
        s.sleep(1)
        # 切换到报价配置
        s.find("#rc-tabs-0-tab-2").click()
        s.sleep(1)
       
    def test_Afpn_1_4(self):
        """
        基础数据-档口配置
        """
        s = Steps()
        s.open(f"{BaseUrl}/basicData/store")
        s.sleep(1)
        # 点击账号管理
        s.find("#app > section > section > main > div:nth-child(2) > div > div.content > div > div > form > div.SCard-module__s-card___jVkOR > div:nth-child(4) > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > button:nth-child(1) > span").click()
        s.sleep(1)
        # 关闭窗口
        s.find("body > div:nth-child(6) > div > div.ant-modal-wrap.ant-modal-centered > div > div.ant-modal-content > button > span > span > svg").click()
        s.sleep(1)


    def test_Afpn_1_5(self):
        """
        基础数据-账号管理
        """
        s = Steps()
        s.open(f"{BaseUrl}/basicData/accountManage")
        s.sleep(1)
        # 选择平台第一个角色
        s.find("#rc_select_0").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div:nth-child(2) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div:nth-child(3) > div > div > div > div > ul > li:nth-child(1) > div.ant-cascader-menu-item-content").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div:nth-child(2) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div:nth-child(3) > div > div > div > div > ul:nth-child(2) > li:nth-child(1) > div").click()
        s.sleep(1)
        # 选择状态
        s.find("#rc_select_1").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div:nth-child(3) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div:nth-child(1)").click()
        s.sleep(1)
        # 点击新增
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div:nth-child(4) > div > div > div > div > div > button:nth-child(2) > span").click()
        s.sleep(1)
        # 输入姓名
        s.find("#form_item_name").type(testdata.username(language="zh"))
        # 输入手机号
        s.find("#form_item_phoneNumber").type(testdata.get_phone())
        # 输入密码
        s.find("#form_item_password").type(testdata.get_digits(6))
        # 点击取消
        s.find("body > div:nth-child(5) > div > div.ant-modal-wrap.ant-modal-centered > div > div.ant-modal-content > div.ant-modal-footer > button.css-jmkaz5.ant-btn.ant-btn-default > span").click()
        s.sleep(1)

    def test_Afpn_2_1(self):
        """
        物料管理-物料分类
        """
        s = Steps()
        s.open(f"{BaseUrl}/materialManage/MaterialCategory")
        s.sleep(1)
        # 添加一级分类
        s.find("#app > section > section > main > div:nth-child(2) > div.s-right.s-m-b-16 > button > span").click()
        s.sleep(1)
        # 输入分类编码，名称
        s.find("#form_item_mcCode").type("88")
        s.find("#form_item_mcName").type("test")
        # 点击确定
        s.find("body > div:nth-child(5) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-footer > button.css-jmkaz5.ant-btn.ant-btn-primary > span").click()
        s.sleep(1)
        self.assertText("物料一级分类添加成功")
        # 搜索添加的分类 并删除
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR > form > div > div:nth-child(1) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > span > input").type("test")
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR > div > div > div > div > div > div > table > tbody > tr.ant-table-row.ant-table-row-level-0 > td.ant-table-cell.ant-table-cell-fix-right.ant-table-cell-fix-right-first > button:nth-child(3) > span").click()
        s.sleep(1)
        # 二次确认
        s.find("body > div:nth-child(6) > div > div > div > div.ant-popover-inner > div > div > div.ant-popconfirm-buttons > button.css-jmkaz5.ant-btn.ant-btn-primary.ant-btn-sm.ant-btn-dangerous > span").click()
        s.sleep(1)
        self.assertText("物料分类删除成功")



    def test_Afpn_2_2(self):
        """
        物料管理-物料品牌
        """
        s = Steps()
        s.open(f"{BaseUrl}/materialManage/materialBrand")
        s.sleep(1)
        # 点击新增
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div.ant-col.ant-col-xs-24.ant-col-sm-24.ant-col-md-16.ant-col-lg-16.ant-col-xl-12.ant-col-xxl-8.SSearchCol-module__s-search-col___5B72G.css-jmkaz5 > div > div > div > div > div > button:nth-child(2) > span").click()
        s.sleep(1)
        # 输入品牌编码名称
        Scode = testdata.get_digits(6)
        s.find("#form_item_brandCode").type(Scode)
        s.find("#form_item_brandName").type(testdata.username(language="zh"))
        # 点击确定
        s.find("body > div:nth-child(5) > div > div.ant-modal-wrap.ant-modal-centered > div > div.ant-modal-content > div.ant-modal-footer > button.css-jmkaz5.ant-btn.ant-btn-primary > span").click()
        s.sleep(1)
        self.assertText("添加成功")
        # 搜索添加的品牌编号 并删除
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div:nth-child(1) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > span > input").type(Scode)
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div:nth-child(2) > div > div > div > div > div > div > table > tbody > tr.ant-table-row.ant-table-row-level-0 > td.ant-table-cell.ant-table-cell-fix-right.ant-table-cell-fix-right-first > button:nth-child(2) > span").click()
        s.sleep(1)
        # 二次确认
        s.find("body > div:nth-child(6) > div > div > div > div.ant-popover-inner > div > div > div.ant-popconfirm-buttons > button.css-jmkaz5.ant-btn.ant-btn-primary.ant-btn-sm.ant-btn-dangerous > span").click()
        s.sleep(1)
        self.assertText("删除成功")




    def test_Afpn_2_3(self):
        """
        物料管理-SPU管理
        """
        s = Steps()
        s.open(f"{BaseUrl}/materialManage/spuManage")
        s.sleep(1)
        # 点击新增
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div.ant-col.ant-col-xs-24.ant-col-sm-24.ant-col-md-16.ant-col-lg-16.ant-col-xl-12.ant-col-xxl-8.SSearchCol-module__s-search-col___5B72G.css-jmkaz5 > div > div > div > div > div > button:nth-child(2) > span").click()
        s.sleep(1)
        # 选择物料分类
        s.find("#app > section > section > main > div:nth-child(2) > form > div > div:nth-child(2) > div > div > div.ant-row.ant-form-item-row.css-jmkaz5 > div.ant-col.ant-form-item-control.css-jmkaz5 > div.ant-form-item-control-input > div > span").click()
        s.sleep(1)
        # 选择第一个分类的二级分类
        s.find("body > div:nth-child(6) > div > div.ant-modal-wrap.ant-modal-centered > div > div.ant-modal-content > div.ant-modal-body > div > div > div > div > div.ant-tree-list > div > div > div > div:nth-child(1) > span.ant-tree-switcher.ant-tree-switcher_close").click()
        s.sleep(1)
        s.find("body > div:nth-child(6) > div > div.ant-modal-wrap.ant-modal-centered > div > div.ant-modal-content > div.ant-modal-body > div > div > div > div > div.ant-tree-list > div > div > div > div:nth-child(2) > span.ant-tree-node-content-wrapper.ant-tree-node-content-wrapper-close > span > div > span").click()
        s.sleep(1)
        # 点击确定
        s.find("body > div:nth-child(6) > div > div.ant-modal-wrap.ant-modal-centered > div > div.ant-modal-content > div.ant-modal-footer > button.css-jmkaz5.ant-btn.ant-btn-primary > span").click()
        s.sleep(1)
        # 输入SPU名称
        Sname = testdata.username(language="zh")
        s.find("#form_item_spuName").type(Sname)
        s.sleep(1)
        # 点击提交
        s.find("#breadcrumb-right > div > button.css-jmkaz5.ant-btn.ant-btn-primary.SButton-module__s-button___IkZHy").click()
        s.sleep(1)
        self.assertText("物料添加成功")
        # 搜索添加的SPU 并删除
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div:nth-child(3) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > span > input").type(Sname)
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div:nth-child(2) > div.ant-table-wrapper.STable-module__s-table___YskNF.css-jmkaz5 > div > div > div > div > div > table > tbody > tr.ant-table-row.ant-table-row-level-0 > td.ant-table-cell.ant-table-cell-fix-right.ant-table-cell-fix-right-first > button:nth-child(3)").click()
        s.sleep(1)
        # 二次确认
        s.find("body > div:nth-child(6) > div > div > div > div.ant-popover-inner > div > div > div.ant-popconfirm-buttons > button.css-jmkaz5.ant-btn.ant-btn-primary.ant-btn-sm.ant-btn-dangerous > span").click()
        s.sleep(1)
        self.assertText("SPU删除成功")



    def test_Afpn_2_4(self):
        """
        物料管理-物料档案
        """
        s = Steps()
        s.open(f"{BaseUrl}/materialManage/materialRecord")
        s.sleep(1)
        # 点击新增
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div.ant-col.ant-col-xs-24.ant-col-sm-24.ant-col-md-16.ant-col-lg-16.ant-col-xl-12.ant-col-xxl-8.SSearchCol-module__s-search-col___5B72G.css-jmkaz5 > div > div > div > div > div > button:nth-child(2) > span").click()
        s.sleep(1)
        # 输入物料名称
        matName = testdata.username(language="zh")
        s.find("#form_item_matName").type(matName)
        # 选择SPU
        s.find("#app > section > section > main > div:nth-child(2) > form > div.SCard-module__s-card___jVkOR > div:nth-child(1) > div:nth-child(3) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > span > input").click()
        s.sleep(1)
        # 选择第一个SPU
        s.find("body > div:nth-child(6) > div > div.ant-modal-wrap.ant-modal-centered > div > div.ant-modal-content > div.ant-modal-body > div > div:nth-child(2) > div:nth-child(2) > div > div > div > div > div > div.ant-table-body > table > tbody > tr:nth-child(2) > td.ant-table-cell.ant-table-cell-fix-left.ant-table-cell-fix-left-last.ant-table-selection-column > label > span > input").click()
        s.sleep(1)
        s.find("body > div:nth-child(6) > div > div.ant-modal-wrap.ant-modal-centered > div > div.ant-modal-content > div.ant-modal-footer > button.css-jmkaz5.ant-btn.ant-btn-primary > span").click()
        s.sleep(1)
        # 选择品牌
        s.find("#app > section > section > main > div:nth-child(2) > form > div.SCard-module__s-card___jVkOR > div:nth-child(2) > div:nth-child(2) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > span > input").click()
        s.sleep(1)
        # 选择第一个品牌
        s.find("body > div:nth-child(7) > div > div.ant-modal-wrap.ant-modal-centered > div > div.ant-modal-content > div.ant-modal-body > div:nth-child(2) > div > div > div > div > div > div.ant-table-body > table > tbody > tr:nth-child(2) > td.ant-table-cell.ant-table-cell-fix-left.ant-table-cell-fix-left-last.ant-table-selection-column > label > span > input").click()
        s.sleep(1)
        s.find("body > div:nth-child(7) > div > div.ant-modal-wrap.ant-modal-centered > div > div.ant-modal-content > div.ant-modal-footer > button.css-jmkaz5.ant-btn.ant-btn-primary > span").click()
        s.sleep(1)
        # 输入规格
        s.find("#form_item_specs").type("测试规格")
        # 主单位选择第一个
        s.find("#form_item_majorUnitId").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > form > div.SCard-module__s-card___jVkOR > div:nth-child(2) > div:nth-child(4) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div:nth-child(1)").click()
        s.sleep(1)
        # 辅单位选择第一个
        s.find("#form_item_minorUnitId").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > form > div.SCard-module__s-card___jVkOR > div:nth-child(2) > div:nth-child(5) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div:nth-child(1)").click()
        s.sleep(1)
        # 主辅单位换算 选择了主辅单位一致，默认就是1比1了
        # s.find("#app > section > section > main > div:nth-child(2) > form > div.SCard-module__s-card___jVkOR > div:nth-child(2) > div:nth-child(6) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > span > div:nth-child(1)").type("1")
        # s.find("#app > section > section > main > div:nth-child(2) > form > div.SCard-module__s-card___jVkOR > div:nth-child(2) > div:nth-child(6) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > span > div:nth-child(3)").type("1")
        # 计重方式选择第一个
        s.find("#form_item_weightType").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > form > div.SCard-module__s-card___jVkOR > div:nth-child(2) > div:nth-child(7) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div:nth-child(2)").click()
        s.sleep(1)
        # 毛净重比例
        s.find("#app > section > section > main > div:nth-child(2) > form > div.SCard-module__s-card___jVkOR > div:nth-child(2) > div:nth-child(9) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > span > div:nth-child(1) > div > div > input").type("1")
        s.find("#app > section > section > main > div:nth-child(2) > form > div.SCard-module__s-card___jVkOR > div:nth-child(2) > div:nth-child(9) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > span > div:nth-child(3) > div > div > input").type("1")
        # 采购计价方式
        s.find("#form_item_purchasePriceType").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > form > div.SCard-module__s-card___jVkOR > div:nth-child(2) > div:nth-child(10) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div:nth-child(1)").click()
        s.sleep(1)
        # 输入保质期
        s.find("#form_item_retentionPeriod").type("30")
        # 出库计价方式
        s.find("#form_item_outboundPriceType").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > form > div.SCard-module__s-card___jVkOR > div:nth-child(2) > div:nth-child(13) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div:nth-child(1)").click()
        s.sleep(1)
        # 备注
        s.find("#form_item_remark").type("测试备注")
        # 点击提交
        s.find("#app > section > section > main > div:nth-child(2) > form > div.ant-form-item.css-jmkaz5.s-m-t-25.s-flex-x-center > div > div > div > div > button.css-jmkaz5.ant-btn.ant-btn-primary.SButton-module__s-button___IkZHy > span").click()
        s.sleep(1)
        self.assertText("物料添加成功")
        # 搜索添加的SPU 并删除
        s.refresh()
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div:nth-child(2) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > span > input").type(matName)
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div:nth-child(2) > div.ant-table-wrapper.STable-module__s-table___YskNF.css-jmkaz5 > div > div > div > div > div > table > tbody > tr.ant-table-row.ant-table-row-level-0 > td.ant-table-cell.ant-table-cell-fix-right.ant-table-cell-fix-right-first > button:nth-child(4) > span").click()
        s.sleep(1)
        # 二次确认
        s.find("body > div:nth-child(5) > div > div > div > div.ant-popover-inner > div > div > div.ant-popconfirm-buttons > button.css-jmkaz5.ant-btn.ant-btn-primary.ant-btn-sm.ant-btn-dangerous > span").click()
        s.sleep(1)
        self.assertText("物料删除成功")



    def test_Afpn_2_5(self):
        """
        物料管理-货源管理
        """
        s = Steps()
        s.open(f"{BaseUrl}/materialManage/sourceManage")
        s.sleep(1)
        # 按供应商添加
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div.ant-col.ant-col-xs-24.ant-col-sm-24.ant-col-md-16.ant-col-lg-16.ant-col-xl-12.ant-col-xxl-8.SSearchCol-module__s-search-col___5B72G.css-jmkaz5 > div > div > div > div > div > button:nth-child(2) > span").click()
        s.sleep(1)
        # 选择第一个供应商
        s.find("#app > section > section > main > div:nth-child(2) > div:nth-child(2) > div > div > div > div > div > div > table > tbody > tr:nth-child(2) > td.ant-table-cell.ant-table-cell-fix-left.ant-table-cell-fix-left-last.ant-table-selection-column > label > span > input").click()
        # 点击下一步
        s.find("#breadcrumb-right > div > button.css-jmkaz5.ant-btn.ant-btn-primary.SButton-module__s-button___IkZHy > span").click()
        s.sleep(1)
        # 选择物料 选择第一个
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16.s-m-t-16 > form > div > div:nth-child(6) > div > div > div > div > div > button:nth-child(2) > span").click()
        s.sleep(1)
        s.find("body > div:nth-child(5) > div > div.ant-modal-wrap.ant-modal-centered > div > div.ant-modal-content > div.ant-modal-body > div > div:nth-child(2) > div:nth-child(2) > div > div > div > div > div > div.ant-table-body > table > tbody > tr:nth-child(2) > td.ant-table-cell.ant-table-cell-fix-left.ant-table-cell-fix-left-last.ant-table-selection-column > label > span > input").click()
        s.sleep(1)
        s.find("body > div:nth-child(5) > div > div.ant-modal-wrap.ant-modal-centered > div > div.ant-modal-content > div.ant-modal-footer > button.css-jmkaz5.ant-btn.ant-btn-primary > span").click()
        s.sleep(1)
        # 点击提交
        s.find("#breadcrumb-right > div > button:nth-child(3) > span").click()
        s.sleep(1)
        self.assertText("货源（按供应商）添加成功")
        # 搜索添加的供应商 并删除
        s.find("#app > section > section > main > div:nth-child(2) > div:nth-child(2) > div.ant-table-wrapper.STable-module__s-table___YskNF.css-jmkaz5 > div > div > div > div > div > table > tbody > tr:nth-child(2) > td.ant-table-cell.ant-table-cell-fix-right.ant-table-cell-fix-right-first > button:nth-child(2) > span").click()
        s.sleep(1)
        # 二次确认
        s.find("body > div:nth-child(5) > div > div > div > div.ant-popover-inner > div > div > div.ant-popconfirm-buttons > button.css-jmkaz5.ant-btn.ant-btn-primary.ant-btn-sm.ant-btn-dangerous > span").click()
        s.sleep(1)
        self.assertText("货源删除成功")


    def test_Afpn_2_6(self):
        """
        物料管理-直送物料
        """
        s = Steps()
        s.open(f"{BaseUrl}/materialManage/directSendMaterial")
        s.sleep(1)
        # 添加物料
        s.find("#app > section > section > main > div:nth-child(2) > div > div > section > main > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div.ant-col.ant-col-xs-24.ant-col-sm-24.ant-col-md-16.ant-col-lg-16.ant-col-xl-12.ant-col-xxl-8.SSearchCol-module__s-search-col___5B72G.css-jmkaz5 > div > div > div > div > div > button:nth-child(2) > span").click()
        s.sleep(1)
        # 选择第一个供应商
        s.find("#app > section > section > main > div:nth-child(2) > div > div > form > div.SCard-module__s-card___jVkOR > div:nth-child(2) > div > div.ant-col.ant-col-md-10.ant-col-lg-8.ant-col-xl-6.ant-form-item-control.css-jmkaz5 > div > div > span > input").click()
        s.sleep(1)
        s.find("body > div:nth-child(6) > div > div.ant-modal-wrap.ant-modal-centered > div > div.ant-modal-content > div.ant-modal-body > div:nth-child(2) > div > div > div > div > div > div > table > tbody > tr:nth-child(2) > td.ant-table-cell.ant-table-cell-fix-left.ant-table-cell-fix-left-last.ant-table-selection-column > label > span > input").click()
        s.sleep(1)
        s.find("body > div:nth-child(6) > div > div.ant-modal-wrap.ant-modal-centered > div > div.ant-modal-content > div.ant-modal-footer > button.css-jmkaz5.ant-btn.ant-btn-primary > span").click()
        s.sleep(1)
        # 输入物料编码 选择第一个
        s.find("#app > section > section > main > div:nth-child(2) > div > div > form > div.SCard-module__s-card___jVkOR > div:nth-child(3) > div > div.ant-col.ant-col-md-10.ant-col-lg-8.ant-col-xl-6.ant-form-item-control.css-jmkaz5 > div > div > span > input").click()
        s.sleep(1)
        s.find("body > div:nth-child(7) > div > div.ant-modal-wrap.ant-modal-centered > div > div.ant-modal-content > div.ant-modal-body > div > div:nth-child(2) > div:nth-child(2) > div > div > div > div > div > div.ant-table-body > table > tbody > tr.ant-table-row.ant-table-row-level-0 > td.ant-table-cell.ant-table-cell-fix-left.ant-table-cell-fix-left-last.ant-table-selection-column > label > span > input").click()
        s.sleep(1)
        s.find("body > div:nth-child(7) > div > div.ant-modal-wrap.ant-modal-centered > div > div.ant-modal-content > div.ant-modal-footer > button.css-jmkaz5.ant-btn.ant-btn-primary > span").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div > div > form > div.ant-form-item.css-jmkaz5.s-m-t-25.s-flex-center.s-nowrap > div > div > div > div > button.css-jmkaz5.ant-btn.ant-btn-primary.SButton-module__s-button___IkZHy > span").click()
        s.sleep(1)
        self.assertText("物料新增成功")
        # 搜索添加的直送物料 并删除
        s.find("#app > section > section > main > div:nth-child(2) > div > div > section > main > div:nth-child(2) > div.ant-table-wrapper.STable-module__s-table___YskNF.css-jmkaz5 > div > div > div > div > div > table > tbody > tr:nth-child(2) > td.ant-table-cell.ant-table-cell-fix-right.ant-table-cell-fix-right-first > button > span").click()
        s.sleep(1)
        s.find("body > div:nth-child(6) > div > div > div > div.ant-popover-inner > div > div > div.ant-popconfirm-buttons > button.css-jmkaz5.ant-btn.ant-btn-primary.ant-btn-sm.ant-btn-dangerous > span").click()
        s.sleep(1)
        self.assertText("删除成功")



    def test_Afpn_2_7(self):
        """
        物料管理-常用物料
        """
        s = Steps()
        s.open(f"{BaseUrl}/materialManage/commonUseMaterial")
        s.sleep(1)
        # 添加物料
        s.find("#app > section > section > main > div:nth-child(2) > div > div > section > main > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div.ant-col.ant-col-xs-24.ant-col-sm-24.ant-col-md-16.ant-col-lg-16.ant-col-xl-12.ant-col-xxl-8.SSearchCol-module__s-search-col___5B72G.css-jmkaz5 > div > div > div > div > div > button:nth-child(2) > span").click()
        s.sleep(1)
        # 选择第一个，确认添加
        s.find("#app > section > section > main > div:nth-child(2) > div:nth-child(2) > div > div > div > div > div > div > table > tbody > tr:nth-child(2) > td.ant-table-cell.ant-table-cell-fix-left.ant-table-cell-fix-left-last.ant-table-selection-column > label > span > input").click()
        s.find("#breadcrumb-right > div > button.css-jmkaz5.ant-btn.ant-btn-primary.SButton-module__s-button___IkZHy > span").click()
        s.sleep(1)
        self.assertText("添加成功")
        # 搜索添加的常用物料 并删除
        s.find("#app > section > section > main > div:nth-child(2) > div > div > section > main > div:nth-child(2) > div.ant-table-wrapper.STable-module__s-table___YskNF.css-jmkaz5 > div > div > div > div > div > table > tbody > tr:nth-child(2) > td.ant-table-cell.ant-table-cell-fix-right.ant-table-cell-fix-right-first > button > span").click()
        s.sleep(1)        
        # 二次确认
        s.find("body > div:nth-child(6) > div > div > div > div.ant-popover-inner > div > div > div.ant-popconfirm-buttons > button.css-jmkaz5.ant-btn.ant-btn-primary.ant-btn-sm.ant-btn-dangerous > span").click()
        s.sleep(1)
        self.assertText("删除成功")


    def test_Afpn_3_1(self):
        """
        价格管理-采购价格
        """
        s = Steps()
        s.open(f"{BaseUrl}/priceManage/purchasePrice")
        s.sleep(1)
        # 点击日常调价
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div:nth-child(9) > div > div > div > div > div > button:nth-child(2) > span").click()
        s.sleep(1)
        # 点击取消
        s.find("#breadcrumb-right > div > button.css-jmkaz5.ant-btn.ant-btn-default.SButton-module__s-button___IkZHy > span").click()
        s.sleep(1)


    def test_Afpn_3_2(self):
        """
        价格管理-出库价格
        """
        s = Steps()
        s.open(f"{BaseUrl}/priceManage/retrievalPrice")
        s.sleep(1)
        # 点击物料调价
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div:nth-child(8) > div > div > div > div > div > button:nth-child(2) > span").click()
        s.sleep(1)
        # 点击物料名称
        s.find("#app > section > section > main > div:nth-child(2) > form > div.SCard-module__s-card___jVkOR > div > div > div:nth-child(1) > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > span > input").click()
        s.sleep(1)
        # 选择第一个 确定
        s.find("body > div:nth-child(6) > div > div.ant-modal-wrap.ant-modal-centered > div > div.ant-modal-content > div.ant-modal-body > div > div:nth-child(2) > div:nth-child(2) > div > div > div > div > div > div.ant-table-body > table > tbody > tr:nth-child(2) > td.ant-table-cell.ant-table-cell-fix-left.ant-table-cell-fix-left-last.ant-table-selection-column > label > span > input").click()
        s.sleep(1)
        s.find("body > div:nth-child(6) > div > div.ant-modal-wrap.ant-modal-centered > div > div.ant-modal-content > div.ant-modal-footer > button.css-jmkaz5.ant-btn.ant-btn-primary > span").click()
        s.sleep(1)
        # 输入调整后出库价 备注
        s.find("#form_item_purchasePrice").type("100")
        s.find("#form_item_remark").type("测试备注")
        # 点击提交
        s.find("#app > section > section > main > div:nth-child(2) > form > div.ant-form-item.css-jmkaz5.s-m-t-25.s-flex-x-center > div > div > div > div > button.css-jmkaz5.ant-btn.ant-btn-primary.SButton-module__s-button___IkZHy > span").click()
        s.sleep(1)
        self.assertText("提交成功")
        # 删除
        s.find("#app > section > section > main > div:nth-child(2) > div:nth-child(2) > div.ant-table-wrapper.STable-module__s-table___YskNF.css-jmkaz5 > div > div > div > div > div > table > tbody > tr:nth-child(2) > td.ant-table-cell.ant-table-cell-fix-right.ant-table-cell-fix-right-first > button:nth-child(3)").click()
        s.sleep(1)
        s.find("body > div:nth-child(6) > div > div.ant-modal-wrap.ant-modal-centered > div > div.ant-modal-content > div.ant-modal-footer > button.css-jmkaz5.ant-btn.ant-btn-primary > span").click()
        s.sleep(1)
        self.assertText("删除成功")



    def test_Afpn_3_3(self):
        """
        价格管理-调价管理
        """
        s = Steps()
        s.open(f"{BaseUrl}/priceManage/adjustPrice")
        s.sleep(1)
        # 选择类型
        s.find("#rc_select_0").click()
        s.sleep(1)
        # 临时调价
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div:nth-child(4) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div:nth-child(2)").click()
        s.sleep(1)
        # 特殊调价
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div:nth-child(4) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div.ant-select-selector > span.ant-select-selection-item").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div:nth-child(4) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div:nth-child(1)").click()
        s.sleep(1)
        # 状态
        s.find("#rc_select_1").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div:nth-child(5) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div:nth-child(1)").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div:nth-child(5) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div.ant-select-selector > span.ant-select-selection-item").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div:nth-child(5) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div:nth-child(2)").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div:nth-child(5) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div.ant-select-selector > span.ant-select-selection-item").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div:nth-child(5) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div:nth-child(3)").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div:nth-child(5) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div.ant-select-selector > span.ant-select-selection-item").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div:nth-child(5) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div:nth-child(4)").click()
        s.sleep(1)


    def test_Afpn_4_1(self):
        """
        采购管理-物料申请单
        """
        s = Steps()
        s.open(f"{BaseUrl}/purchaseManage/materialApplication")
        s.sleep(1)
        # 新增申购申请
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div:nth-child(7) > div > div > div > div > div > button:nth-child(2) > span").click()
        s.sleep(1)
        # 选择所属商户
        s.find("#form_item_merchantId").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div > div > form > div > div:nth-child(1) > div.ant-row.css-jmkaz5 > div:nth-child(2) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div > div").click()
        s.sleep(1)
        # 选择档口
        s.find("#form_item_storeId").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div > div > form > div > div:nth-child(1) > div.ant-row.css-jmkaz5 > div:nth-child(3) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div:nth-child(1)").click()
        s.sleep(1)
        # 需求日期 选择今天
        s.find("#form_item_requireDate").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div > div > form > div > div:nth-child(1) > div.ant-row.css-jmkaz5 > div:nth-child(5) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div:nth-child(3) > div > div > div > div > div > div.ant-picker-footer > a").click()
        s.sleep(1)
        # 添加
        s.find("#app > section > section > main > div:nth-child(2) > div > div > form > div > div:nth-child(2) > div.s-flex-yox-center.s-flex-x-between > div.s-gap-5-10.s-flex-x-right.s-m-l-10.STitle-module__title-right___NIV-4 > button:nth-child(1) > span").click()
        s.sleep(1)
        # 选择第一个 确定
        s.find("body > div:nth-child(5) > div > div.ant-modal-wrap.ant-modal-centered > div > div.ant-modal-content > div.ant-modal-body > div > div:nth-child(2) > div:nth-child(2) > div > div > div > div > div > div.ant-table-body > table > tbody > tr:nth-child(2) > td.ant-table-cell.ant-table-cell-fix-left.ant-table-cell-fix-left-last.ant-table-selection-column > label > span > input").click()
        s.sleep(1)
        s.find("body > div:nth-child(5) > div > div.ant-modal-wrap.ant-modal-centered > div > div.ant-modal-content > div.ant-modal-footer > button.css-jmkaz5.ant-btn.ant-btn-primary > span").click()
        s.sleep(1)
        # 需求量
        s.find("#form_item_detailList_0_majorQty").type("100")
        s.sleep(1)
        # 保存
        s.find("#breadcrumb-right > div > button:nth-child(2) > span").click()
        s.sleep(1)
        self.assertText("保存成功")

    
    def test_Afpn_4_2(self):
        """
        采购管理-竞价采购
        """
        s = Steps()
        s.open(f"{BaseUrl}/purchaseManage/competition")
        s.sleep(1)
        # 新增
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div:nth-child(7) > div > div > div > div > div > button:nth-child(2) > span").click()
        s.sleep(1)
        # 输入竞价采购单名称
        biddingName = testdata.username(language="zh")
        s.find("#form_item_biddingName").type(biddingName)
        # 报价截止日期 今天
        s.find("#form_item_quotationDeadline").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div > div > form > div > div:nth-child(1) > div.ant-row.css-jmkaz5 > div:nth-child(4) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div:nth-child(3) > div > div > div > div > div > div.ant-picker-footer > a").click()
        s.sleep(1)
        # 需求开始日期
        s.find("#form_item_requireDateStart").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div > div > form > div > div:nth-child(1) > div.ant-row.css-jmkaz5 > div:nth-child(5) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div:nth-child(3) > div > div > div > div > div > div.ant-picker-footer > a").click()
        s.sleep(1)
        # 需求结束日期
        s.find("#form_item_requireDateEnd").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div > div > form > div > div:nth-child(1) > div.ant-row.css-jmkaz5 > div:nth-child(6) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div:nth-child(3) > div > div > div > div > div > div.ant-picker-footer > a").click()
        s.sleep(1)
        # 中标后结算规则
        s.find("#form_item_settlementRuleType").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div > div > form > div > div:nth-child(1) > div.ant-row.css-jmkaz5 > div:nth-child(7) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div:nth-child(1)").click()
        s.sleep(1)
        # 添加物料
        s.find("#app > section > section > main > div:nth-child(2) > div > div > form > div > div:nth-child(2) > div.s-flex-yox-center.s-flex-x-between > div.s-gap-5-10.s-flex-x-right.s-m-l-10.STitle-module__title-right___NIV-4 > button > span").click()
        s.sleep(1)
        # 选择第一个 确定
        s.find("body > div:nth-child(5) > div > div.ant-modal-wrap.ant-modal-centered > div > div.ant-modal-content > div.ant-modal-body > div > div:nth-child(2) > div:nth-child(2) > div > div > div > div > div > div.ant-table-body > table > tbody > tr:nth-child(2) > td.ant-table-cell.ant-table-cell-fix-left.ant-table-cell-fix-left-last.ant-table-selection-column > label > span > input").click()
        s.sleep(1)
        s.find("body > div:nth-child(5) > div > div.ant-modal-wrap.ant-modal-centered > div > div.ant-modal-content > div.ant-modal-footer > button.css-jmkaz5.ant-btn.ant-btn-primary > span").click()
        s.sleep(1)
        # 输入计划采购数量
        s.find("#form_item_itemResultList_0_minorQty").type("100")
        s.find("#form_item_itemResultList_0_majorQty").type("100")
        s.sleep(1)
        # 保存
        s.find("#breadcrumb-right > div > button:nth-child(2) > span").click()
        s.sleep(1)
        self.assertText("保存成功")
        # 删除
        s.find("#app > section > section > main > div:nth-child(2) > div:nth-child(2) > div > div > div > div > div > div > table > tbody > tr:nth-child(2) > td.ant-table-cell.ant-table-cell-fix-right.ant-table-cell-fix-right-first > button:nth-child(4) > span").click()
        s.sleep(1)
        s.find("body > div:nth-child(5) > div > div > div > div.ant-popover-inner > div > div > div.ant-popconfirm-buttons > button.css-jmkaz5.ant-btn.ant-btn-primary.ant-btn-sm.ant-btn-dangerous > span").click()
        s.sleep(1)
        self.assertText("删除成功")


    def test_Afpn_4_3(self):
        """
        采购管理-报价采购
        """
        s = Steps()
        s.open(f"{BaseUrl}/purchaseManage/quotation")
        s.sleep(1)
        # 新增
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div:nth-child(7) > div > div > div > div > div > button:nth-child(2) > span").click()
        s.sleep(1)
        # 所属商户
        s.find("#form_item_merchantId").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div > div > form > div > div > div:nth-child(3) > div > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div > div").click()
        s.sleep(1)
        # 报价采购单名单
        biddingName = testdata.username(language="zh")
        s.find("#form_item_biddingName").type(biddingName)
        # 报价截止日期
        s.find("#form_item_quotationDeadline").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div > div > form > div > div > div:nth-child(5) > div > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div:nth-child(3) > div > div > div > div > div > div.ant-picker-footer > a").click()
        s.sleep(1)
        # 需求开始日期
        s.find("#form_item_requireDateStart").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div > div > form > div > div > div:nth-child(6) > div > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div:nth-child(3) > div > div > div > div > div > div.ant-picker-footer > a").click()
        s.sleep(1)
        # 需求结束日期
        s.find("#form_item_requireDateEnd").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div > div > form > div > div > div:nth-child(7) > div > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div:nth-child(3) > div > div > div > div > div > div.ant-picker-footer > a").click()
        s.sleep(1)
        # 备注
        s.find("#form_item_remark").type("测试备注")
        s.sleep(1)
        # 下一步
        s.find("#breadcrumb-right > div > button.css-jmkaz5.ant-btn.ant-btn-primary.SButton-module__s-button___IkZHy").click()
        s.sleep(1)
        # 物料清单新增
        s.find("#rc-tabs-1-panel-0 > form > div > div.ant-col.ant-col-xs-24.ant-col-sm-24.ant-col-md-16.ant-col-lg-16.ant-col-xl-12.ant-col-xxl-8.SSearchCol-module__s-search-col___5B72G.css-jmkaz5 > div > div > div > div > div > button:nth-child(2) > span").click()
        s.sleep(1)
        # 选择第一个 确定
        s.find("body > div:nth-child(5) > div > div.ant-modal-wrap.ant-modal-centered > div > div.ant-modal-content > div.ant-modal-body > div > div:nth-child(2) > div:nth-child(2) > div > div > div > div > div > div.ant-table-body > table > tbody > tr:nth-child(2) > td.ant-table-cell.ant-table-cell-fix-left.ant-table-cell-fix-left-last.ant-table-selection-column > label > span > input").click()
        s.sleep(1)
        s.find("body > div:nth-child(5) > div > div.ant-modal-wrap.ant-modal-centered > div > div.ant-modal-content > div.ant-modal-footer > button.css-jmkaz5.ant-btn.ant-btn-primary > span").click()
        s.sleep(2)
        # 数量  
        s.find("#rc-tabs-1-panel-0 > div > div > div > div > div > div > table > tbody > tr.ant-table-row.ant-table-row-level-0 > td:nth-child(3) > div > div > div > div > div > div > div > input").type("100")
        s.sleep(1)
        # 备注
        s.find("#rc-tabs-1-panel-0 > div > div > div > div > div > div > table > tbody > tr.ant-table-row.ant-table-row-level-0 > td:nth-child(5) > span > input").type("测试备注")
        s.sleep(1) 
        # 选择单位 第一个 确定
        s.find("#rc-tabs-1-panel-0 > div > div > div > div > div > div > table > tbody > tr.ant-table-row.ant-table-row-level-0 > td:nth-child(4) > div > div > div > div > div").click()
        s.sleep(1)
        s.find("body > div:nth-child(6) > div > div.ant-modal-wrap.ant-modal-centered > div > div.ant-modal-content > div.ant-modal-body > div:nth-child(2) > div > div > div > div > div > div.ant-table-body > table > tbody > tr:nth-child(2) > td.ant-table-cell.ant-table-cell-fix-left.ant-table-cell-fix-left-last.ant-table-selection-column > label > span > input").click()
        s.sleep(1)
        s.find("body > div:nth-child(6) > div > div.ant-modal-wrap.ant-modal-centered > div > div.ant-modal-content > div.ant-modal-footer > button.css-jmkaz5.ant-btn.ant-btn-primary > span").click()
        s.sleep(1)
        # 保存
        s.find("#breadcrumb-right > div > button:nth-child(3) > span").click()
        s.sleep(1)
        self.assertText("保存成功")
        # 删除
        s.find("#app > section > section > main > div:nth-child(2) > div:nth-child(2) > div.ant-table-wrapper.STable-module__s-table___YskNF.css-jmkaz5 > div > div > div > div > div > table > tbody > tr:nth-child(2) > td.ant-table-cell.ant-table-cell-fix-right.ant-table-cell-fix-right-first > button:nth-child(3) > span").click()
        s.sleep(1)
        s.find("body > div:nth-child(5) > div > div > div > div.ant-popover-inner > div > div > div.ant-popconfirm-buttons > button.css-jmkaz5.ant-btn.ant-btn-primary.ant-btn-sm.ant-btn-dangerous > span").click()
        s.sleep(1)
        self.assertText("删除成功")



    def test_Afpn_4_4(self):
        """
        采购管理-采购订单
        """
        s = Steps()
        s.open(f"{BaseUrl}/purchaseManage/purchaseOrder")
        s.sleep(1)
        # 统一采购
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div.ant-col.ant-col-xs-24.ant-col-sm-24.ant-col-md-24.ant-col-lg-24.ant-col-xl-18.ant-col-xxl-12.SSearchCol-module__s-search-col___5B72G.css-jmkaz5 > div > div > div > div > div > button:nth-child(2) > span").click()
        s.sleep(1)
        # 所属商户
        s.find("#form_item_merchantId").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div > div > form > div > div:nth-child(1) > div.ant-row.css-jmkaz5 > div:nth-child(1) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div > div").click()
        s.sleep(1)
        # 需求日期 今日
        s.find("#form_item_requireDate").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div > div > form > div > div:nth-child(1) > div.ant-row.css-jmkaz5 > div:nth-child(4) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div:nth-child(3) > div > div > div > div > div > div.ant-picker-footer > a").click()
        s.sleep(1)
        # 仓库 第一个
        s.find("#form_item_warehouseId").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div > div > form > div > div:nth-child(1) > div.ant-row.css-jmkaz5 > div:nth-child(5) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div:nth-child(1)").click()
        s.sleep(1)
        # 配送点
        s.find("#form_item_deliverAddressId").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div > div > form > div > div:nth-child(1) > div.ant-row.css-jmkaz5 > div:nth-child(6) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div:nth-child(1)").click()
        s.sleep(1)
        # 添加物料 选择第一个 确定
        s.find("#app > section > section > main > div:nth-child(2) > div > div > form > div > div:nth-child(2) > div.s-flex-yox-center.s-flex-x-between > div.s-gap-5-10.s-flex-x-right.s-m-l-10.STitle-module__title-right___NIV-4 > button:nth-child(2) > span").click()
        s.sleep(1)
        s.find("body > div:nth-child(5) > div > div.ant-modal-wrap.ant-modal-centered > div > div.ant-modal-content > div.ant-modal-body > div > div:nth-child(2) > div:nth-child(2) > div > div > div > div > div > div.ant-table-body > table > tbody > tr:nth-child(2) > td.ant-table-cell.ant-table-cell-fix-left.ant-table-cell-fix-left-last.ant-table-selection-column > label > span > input").click()
        s.sleep(1)
        s.find("body > div:nth-child(5) > div > div.ant-modal-wrap.ant-modal-centered > div > div.ant-modal-content > div.ant-modal-footer > button.css-jmkaz5.ant-btn.ant-btn-primary > span").click()
        s.sleep(1)
        # 选择供应商 第一个 确定
        s.find("#app > section > section > main > div:nth-child(2) > div > div > form > div > div:nth-child(2) > div.ant-table-wrapper.STable-module__s-table___YskNF.css-jmkaz5 > div > div > div > div > div > table > tbody > tr.ant-table-row.ant-table-row-level-0 > td:nth-child(13) > div > div > div > div > div > span > input").click()
        s.sleep(1)
        s.find("body > div:nth-child(6) > div > div.ant-modal-wrap.ant-modal-centered > div > div.ant-modal-content > div.ant-modal-body > div:nth-child(2) > div > div > div > div > div > div > table > tbody > tr.ant-table-row.ant-table-row-level-0 > td.ant-table-cell.ant-table-cell-fix-left.ant-table-cell-fix-left-last.ant-table-selection-column > label > span > input").click()
        s.sleep(1)
        s.find("body > div:nth-child(6) > div > div.ant-modal-wrap.ant-modal-centered > div > div.ant-modal-content > div.ant-modal-footer > button.css-jmkaz5.ant-btn.ant-btn-primary > span").click()
        s.sleep(1)
        # 输入采购量
        s.find("#form_item_detailParams_0_minorQty").type("100")
        s.sleep(1)
        s.find("#form_item_detailParams_0_majorQty").type("100")
        s.sleep(1)
        # 保存
        s.find("#breadcrumb-right > div > button:nth-child(2) > span").click()
        s.sleep(1)
        self.assertText("保存成功")
        # 删除
        s.find("#app > section > section > main > div:nth-child(2) > div:nth-child(2) > div.ant-table-wrapper.STable-module__s-table___YskNF.css-jmkaz5 > div > div > div > div > div > table > tbody > tr:nth-child(2) > td.ant-table-cell.ant-table-cell-fix-right.ant-table-cell-fix-right-first > button:nth-child(4) > span").click()
        s.sleep(1)
        s.find("body > div:nth-child(5) > div > div > div > div.ant-popover-inner > div > div > div.ant-popconfirm-buttons > button.css-jmkaz5.ant-btn.ant-btn-primary.ant-btn-sm.ant-btn-dangerous > span").click()
        s.sleep(1)
        self.assertText("删除成功")



    def test_Afpn_4_5(self):
        """
        采购管理-结算主体
        """
        s = Steps()
        s.open(f"{BaseUrl}/purchaseManage/purchasePrincipal")
        s.sleep(1)
        # 状态
        s.find("#rc_select_0").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div:nth-child(3) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div:nth-child(1)").click()
        s.sleep(1)
        

    def test_Afpn_5_1(self):
        """
        库存管理-验收管理
        """
        s = Steps()
        s.open(f"{BaseUrl}/stockManage/inboundAcceptance")
        s.sleep(1)
        # 所属商户
        s.find("#rc_select_0").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div:nth-child(1) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div > div").click()
        s.sleep(1)
        # 档口名称
        s.find("#rc_select_1").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div:nth-child(2) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div:nth-child(1)").click()
        s.sleep(1)
        # 供应商
        s.find("#rc_select_2").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div:nth-child(3) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div:nth-child(1)").click()
        s.sleep(1)
        # 收货状态
        s.find("#rc_select_3").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div:nth-child(7) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div:nth-child(1)").click()
        s.sleep(1)


    def test_Afpn_5_2(self):
        """
        库存管理-领用管理
        """
        s = Steps()
        s.open(f"{BaseUrl}/stockManage/outboundPickOut")
        s.sleep(1)
        # 所属商户
        s.find("#rc_select_0").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div:nth-child(1) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div > div").click()
        s.sleep(1)
        # 状态
        s.find("#rc_select_1").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div:nth-child(3) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div:nth-child(1)").click()
        s.sleep(1)



    def test_Afpn_5_3(self):
        """
        库存管理-入库单
        """
        s = Steps()
        s.open(f"{BaseUrl}/stockManage/inboundReceipt")
        s.sleep(1)
        # 所属商户
        s.find("#rc_select_0").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div:nth-child(1) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div > div").click()
        s.sleep(1)
        # 档口名称
        s.find("#rc_select_1").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div:nth-child(2) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div:nth-child(1)").click()
        s.sleep(1)
        # 单据状态
        s.find("#rc_select_2").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div:nth-child(5) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div:nth-child(2)").click()
        s.sleep(1)


    def test_Afpn_5_4(self):
        """
        库存管理-出库单
        """
        s = Steps()
        s.open(f"{BaseUrl}/stockManage/outboundReceipt")
        s.sleep(1)
        # 所属商户
        s.find("#rc_select_0").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div:nth-child(1) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div > div").click()
        s.sleep(1)
        # 档口名称
        s.find("#rc_select_1").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div:nth-child(2) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div:nth-child(1)").click()
        s.sleep(1)
        # 单据状态
        s.find("#rc_select_2").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div:nth-child(4) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div:nth-child(2)").click()
        s.sleep(1)



    def test_Afpn_5_5(self):
        """
        库存管理-库存查询
        """
        s = Steps()
        s.open(f"{BaseUrl}/stockManage/stockSearch")
        s.sleep(1)
        # 所属商户
        s.find("#rc_select_0").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div:nth-child(1) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div > div").click()
        s.sleep(1)
        # 仓库
        s.find("#rc_select_1").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div:nth-child(2) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div:nth-child(1)").click()
        s.sleep(1)


    def test_Afpn_5_6(self):
        """
        库存管理-库存流水查询
        """
        s = Steps()
        s.open(f"{BaseUrl}/stockManage/stockJournalizing")
        s.sleep(1)
        # 所属商户
        s.find("#rc_select_0").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div:nth-child(1) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div > div").click()
        s.sleep(1)
        # 仓库
        s.find("#rc_select_1").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div:nth-child(2) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div:nth-child(1)").click()
        s.sleep(1)
        # 类型
        s.find("#rc_select_2").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div:nth-child(7) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div:nth-child(1)").click()
        s.sleep(1)



    def test_Afpn_5_7(self):
        """
        库存管理-预警配置
        """
        s = Steps()
        s.open(f"{BaseUrl}/stockManage/alertConfig")
        s.sleep(1)
        # 新增
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div:nth-child(7) > div > div > div > div > div > button:nth-child(2) > span").click()
        s.sleep(1)
        # 所属商户
        s.find("#form_item_merchantId").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div > div > form > div.SCard-module__s-card___jVkOR.s-g-b-32 > div > div:nth-child(2) > div:nth-child(1) > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div > div").click()
        s.sleep(1)
        # 仓库名称
        s.find("#form_item_warehouseId").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div > div > form > div.SCard-module__s-card___jVkOR.s-g-b-32 > div > div:nth-child(2) > div:nth-child(2) > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div:nth-child(1)").click()
        s.sleep(1)
        # 物料编码 选择第一个 确定
        s.find("#app > section > section > main > div:nth-child(2) > div > div > form > div.SCard-module__s-card___jVkOR.s-g-b-32 > div > div:nth-child(2) > div:nth-child(3) > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > span > input").click()
        s.sleep(1)
        s.find("body > div:nth-child(5) > div > div.ant-modal-wrap.ant-modal-centered > div > div.ant-modal-content > div.ant-modal-body > div > div:nth-child(2) > div:nth-child(2) > div > div > div > div > div > div.ant-table-body > table > tbody > tr:nth-child(2) > td.ant-table-cell.ant-table-cell-fix-left.ant-table-cell-fix-left-last.ant-table-selection-column > label > span > input").click()
        s.sleep(1)
        s.find("body > div:nth-child(5) > div > div.ant-modal-wrap.ant-modal-centered > div > div.ant-modal-content > div.ant-modal-footer > button.css-jmkaz5.ant-btn.ant-btn-primary > span").click()
        s.sleep(1)
        num = self.get_attribute(css="#app > section > section > main > div:nth-child(2) > div > div > form > div.SCard-module__s-card___jVkOR.s-g-b-32 > div > div:nth-child(2) > div:nth-child(3) > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > span.ant-input-affix-wrapper.ant-input-affix-wrapper-readonly.ant-input-affix-wrapper-status-success.css-jmkaz5 > input", attribute="value")
        print(f"物料编码：{num}")
        # 最低库存量
        s.find("#app > section > section > main > div:nth-child(2) > div > div > form > div.SCard-module__s-card___jVkOR.s-g-b-32 > div > div:nth-child(2) > div:nth-child(4) > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > span > div:nth-child(1) > div > div > input").type("10")
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div > div > form > div.SCard-module__s-card___jVkOR.s-g-b-32 > div > div:nth-child(2) > div:nth-child(4) > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > span > div:nth-child(4) > div > div > input").type("20")
        s.sleep(1)
        # 点击提交
        s.find("#app > section > section > main > div:nth-child(2) > div > div > form > div.ant-form-item.css-jmkaz5.s-flex-center.s-nowrap > div > div > div > div > button.css-jmkaz5.ant-btn.ant-btn-primary.SButton-module__s-button___IkZHy").click()
        s.sleep(1)
        # 搜索后，进行删除
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div:nth-child(1) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > span > input").type(num)
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div:nth-child(2) > div.ant-table-wrapper.STable-module__s-table___YskNF.css-jmkaz5 > div > div > div > div > div > table > tbody > tr.ant-table-row.ant-table-row-level-0 > td.ant-table-cell.ant-table-cell-fix-right.ant-table-cell-fix-right-first > button:nth-child(2) > span").click()
        s.sleep(1)
        s.find("body > div:nth-child(5) > div > div > div > div.ant-popover-inner > div > div > div.ant-popconfirm-buttons > button.css-jmkaz5.ant-btn.ant-btn-primary.ant-btn-sm.ant-btn-dangerous > span").click()
        s.sleep(1)
        self.assertText("删除成功")



    def test_Afpn_5_8(self):
        """
        库存管理-仓库
        """
        s = Steps()
        s.open(f"{BaseUrl}/stockManage/wareHouse")
        s.sleep(1)
        # 点击新增
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div:nth-child(4) > div > div > div > div > div > button:nth-child(2) > span").click()
        s.sleep(1)
        # 商户名称
        s.find("#form_item_merchantId").click()
        s.sleep(1)
        s.find("body > div:nth-child(5) > div > div.ant-modal-wrap.ant-modal-centered > div > div.ant-modal-content > div.ant-modal-body > form > div:nth-child(1) > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div").click()
        s.sleep(1)
        # 输入仓库编码
        item_code = testdata.get_digits(6)
        s.find("#form_item_code").type(item_code)
        # 输入仓库名称
        item_name = testdata.username(language="zh")
        s.find("#form_item_name").type(item_name)
        # 输入地址
        s.find("#form_item_address").type("测试地址")
        # 点击提交
        s.find("body > div:nth-child(5) > div > div.ant-modal-wrap.ant-modal-centered > div > div.ant-modal-content > div.ant-modal-footer > button.css-jmkaz5.ant-btn.ant-btn-primary > span").click()
        s.sleep(1)
        self.assertText("添加成功")
        # 输入仓库名称，删除
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div:nth-child(2) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > span > input").type(item_name)
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div:nth-child(2) > div > div > div > div > div > div > table > tbody > tr.ant-table-row.ant-table-row-level-0 > td.ant-table-cell.ant-table-cell-fix-right.ant-table-cell-fix-right-first > button:nth-child(3) > span").click()
        s.sleep(1)
        s.find("body > div:nth-child(6) > div > div > div > div.ant-popover-inner > div > div > div.ant-popconfirm-buttons > button.css-jmkaz5.ant-btn.ant-btn-primary.ant-btn-sm.ant-btn-dangerous > span").click()
        s.sleep(1)
        self.assertText("删除成功")



    def test_Afpn_5_9(self):
        """
        库存管理-配送点
        """
        s = Steps()
        s.open(f"{BaseUrl}/stockManage/distributionSite")
        s.sleep(1)
        # 点击新增
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div:nth-child(4) > div > div > div > div > div > button:nth-child(2) > span").click()
        s.sleep(1)
        # 商户名称
        s.find("#form_item_merchantId").click()
        s.sleep(1)
        s.find("body > div:nth-child(5) > div > div.ant-modal-wrap.ant-modal-centered > div > div.ant-modal-content > div.ant-modal-body > form > div:nth-child(1) > div > div.ant-col.ant-col-12.ant-form-item-control.css-jmkaz5 > div > div > div > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div > div").click()
        s.sleep(1)
        # 输入配送点编码
        deliverAddrCode = testdata.get_digits(8)
        s.find("#form_item_deliverAddrCode").type(deliverAddrCode)
        # 输入配送点名称
        deliverAddrName = testdata.username(language="zh")
        s.find("#form_item_deliverAddrName").type(deliverAddrName)
        # 输入配送地址
        s.find("#form_item_address").type("测试地址")
        # 仓库名称
        s.find("#form_item_warehouseId").click()
        s.sleep(1)
        s.find("body > div:nth-child(5) > div > div.ant-modal-wrap.ant-modal-centered > div > div.ant-modal-content > div.ant-modal-body > form > div:nth-child(5) > div > div.ant-col.ant-col-12.ant-form-item-control.css-jmkaz5 > div > div > div > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div:nth-child(1)").click()
        s.sleep(1)
        # 点击确定
        s.find("body > div:nth-child(5) > div > div.ant-modal-wrap.ant-modal-centered > div > div.ant-modal-content > div.ant-modal-footer > button.css-jmkaz5.ant-btn.ant-btn-primary > span").click()
        s.sleep(1)
        self.assertText("添加成功")
        # 输入配送点名称，删除
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div:nth-child(2) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > span > input").type(deliverAddrName)
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div:nth-child(2) > div > div > div > div > div > div > table > tbody > tr.ant-table-row.ant-table-row-level-0 > td.ant-table-cell.ant-table-cell-fix-right.ant-table-cell-fix-right-first > button:nth-child(3) > span").click()
        s.sleep(1)
        s.find("body > div:nth-child(6) > div > div > div > div.ant-popover-inner > div > div > div.ant-popconfirm-buttons > button.css-jmkaz5.ant-btn.ant-btn-primary.ant-btn-sm.ant-btn-dangerous > span").click()
        s.sleep(1)
        self.assertText("删除成功")



    def test_Afpn_6_1(self):
        """
        财务管理-供应商对账
        """
        s = Steps()
        s.open(f"{BaseUrl}/financeManage/supplierReconciliation")
        s.sleep(1)
        # 商户名称
        s.find("#form_item_merchantId").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > form > div.SCard-module__s-card___jVkOR > div > div > div > div.ant-row.ant-form-item-row.css-jmkaz5 > div.ant-col.ant-form-item-control.css-jmkaz5 > div.ant-form-item-control-input > div > div > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div").click()
        s.sleep(1)
        # 对账月份
        s.find("#form_item_checkDate").click()
        s.sleep(1)
        s.find("body > div:nth-child(5) > div > div > div > div > div > div > div.ant-picker-body > table > tbody > tr:nth-child(4) > td:nth-child(3) > div").click()
        s.sleep(1)
        # 点击统计对账数据
        s.find("#app > section > section > main > div:nth-child(2) > form > div.ant-form-item.css-jmkaz5.s-m-t-25.s-flex-x-center > div > div > div > div > button > span").click()
        s.sleep(1)
        # 点击取消
        s.find("#app > section > section > main > div:nth-child(2) > div > div.check_button > button.css-jmkaz5.ant-btn.ant-btn-default.SButton-module__s-button___IkZHy > span").click()
        s.sleep(1)


    def test_Afpn_6_2(self):
        """
        财务管理-验收统计
        """
        s = Steps()
        s.open(f"{BaseUrl}/financeManage/acceptanceStatistics")
        s.sleep(1)
        # 所属商户
        s.find("#rc_select_0").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div:nth-child(1) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div > div").click()
        s.sleep(1)
        # 供应商名称
        s.find("#rc_select_1").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div:nth-child(2) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div:nth-child(1)").click()
        s.sleep(1)
        

    def test_Afpn_6_3(self):
        """
        财务管理-档口对账
        """
        s = Steps()
        s.open(f"{BaseUrl}/financeManage/storeReconciliation")
        s.sleep(1)
        # 供应商名称
        s.find("#form_item_merchantId").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > form > div.SCard-module__s-card___jVkOR > div > div > div:nth-child(1) > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div > div").click()
        s.sleep(1)
        # 选择对账月份
        s.find("#form_item_checkDate").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > form > div.SCard-module__s-card___jVkOR > div > div > div:nth-child(3) > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div:nth-child(3) > div > div > div > div > div > div > div.ant-picker-body > table > tbody > tr:nth-child(4) > td:nth-child(3) > div").click()
        s.sleep(1)
        # 统计对账数据
        s.find("#app > section > section > main > div:nth-child(2) > form > div.ant-form-item.css-jmkaz5.s-m-t-25.s-flex-x-center > div > div > div > div > button > span").click()
        s.sleep(1)
        # 取消
        s.find("#breadcrumb-right > div > button.css-jmkaz5.ant-btn.ant-btn-default.SButton-module__s-button___IkZHy > span").click()
        s.sleep(1)
        

    def test_Afpn_7_1(self):
        """
        数据报表-档口领用统计
        """
        s = Steps()
        s.open(f"{BaseUrl}/dataReport/storeReceiveStatistics")
        s.sleep(1)
        # 所属商户
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div:nth-child(1) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div > div").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div:nth-child(1) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div:nth-child(2) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div > div").click()
        s.sleep(1)
        # 档口名称
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div:nth-child(2) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div > div").click()
        s.sleep(1)
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div:nth-child(2) > div > div > div.ant-col.ant-form-item-control.css-jmkaz5 > div > div > div > div:nth-child(2) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div:nth-child(1)").click()
        s.sleep(1)
        # 点击查询
        s.find("#app > section > section > main > div:nth-child(2) > div.SCard-module__s-card___jVkOR.s-m-b-16 > form > div > div:nth-child(4) > div > div > div > div > div > button").click()
        s.sleep(1)
        

    def test_Afpn_8_1(self):
        """
        导入导出-导入管理
        """
        s = Steps()
        s.open(f"{BaseUrl}/dataCenter/importedFiles")
        s.sleep(1)


    def test_Afpn_8_2(self):
        """
        导入导出-导出管理
        """
        s = Steps()
        s.open(f"{BaseUrl}/dataCenter/exportedFiles")
        s.sleep(1)
    


if __name__ == '__main__':
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--headless=new")  # 开启 headless 模式
    browser = {
        "browser": "chrome",
        "options": chrome_options
    }
    seldom.main(
                case='test_apfn_3.AfpnTest', 
                browser=browser,  # 浏览器驱动
                # browser="gc", 
                # browser="firefox",
                tester="tzk",
                # debug=True
                )