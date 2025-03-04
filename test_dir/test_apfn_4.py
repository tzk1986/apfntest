import seldom
from seldom import Steps
from selenium.webdriver import ChromeOptions
import requests


# 测试环境 数字餐厅
BaseUrl = "http://10.50.11.120:9002"

BaseUrl_1 = "http://10.50.11.120:9001"

# 预发布环境
# BaseUrl = ""

# 搜索商户
MerchantName = "艾佩"


class AfpnTest(seldom.TestCase):
    """
    数字餐厅
    """

    value = None

    def start(self):
        print("开始测试")

    def end(self):
        print("结束测试")

    def test_Afpn_001_1(self):
        """
        登录
        """
        print(f"{BaseUrl}/login")
        s = Steps().open(f"{BaseUrl}/login")

        s.find("#app > div > div.login-box.s-h-center > form > div:nth-child(2) > div > div > input").type(
            "18335161013"
        )
        s.find("#app > div > div.login-box.s-h-center > form > div:nth-child(3) > div > div > input").type(
            "112233"
        )
        s.find(
            "#app > div > div.login-box.s-h-center > form > div:nth-child(4) > div > div > div.login-input-code.el-input.el-input--prefix > input"
        ).type("1")
        s.find("#app > div > div.login-box.s-h-center > form > div:nth-child(5) > div > button").click()
        s.sleep()
        self.get_cookies()
        print(self.get_cookies())
        s.open(f"{BaseUrl}/merchant/merchantList")
        s.sleep()
        # 商户简称搜索
        s.find(
            "#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div.search_option_left.s-gap-6-15 > div:nth-child(2) > div > input"
        ).type(f"{MerchantName}")
        s.sleep()
        # 选择跳转到餐厅
        s.find(
            "#app > section > section > section > main > section > section > main > div.main > div.table_content > div.el-table.el-table--fit.el-table--scrollable-x.el-table--enable-row-transition > div.el-table__fixed-right > div.el-table__fixed-body-wrapper > table > tbody > tr > td.el-table_1_column_7.el-table__cell > div > button:nth-child(4) > span"
        ).click()
        s.sleep(2)
        s.switch_to_window(1)
        self.get_cookies()
        print(self.get_cookies())

    def test_Afpn_002_1(self):
        """
        会员-会员列表
        """
        s = Steps().open(f"{BaseUrl_1}/vip/vip/list")
        s.sleep()
        self.assertStatusOk()
        s.find(
            "#app > section > section > section > main > div.main > div.s-card > div > div.search_option_left.s-gap-6-15 > div.s-gap-6-10.s-g-l-0 > button > span"    
        ).click()
        s.sleep()
        # 列表查询
        r = requests.post(
            f"{BaseUrl_1}/api/query/userInfos",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_002_2(self):
        """
        会员-人脸列表
        """
        s = Steps().open(f"{BaseUrl_1}/vip/face/list")
        s.sleep()
        self.assertStatusOk()
        s.find(
            "#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div > div.s-gap-6-10.s-g-l-0 > button"
        ).click()
        s.sleep()
        # 列表查询
        r = requests.post(
            f"{BaseUrl_1}/api/faceAi/getUserInfos",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_003_1(self):
        """
        合作-合作商
        """
        s = Steps().open(f"{BaseUrl_1}/cooperation/cooperation/partner")
        s.sleep()
        self.assertStatusOk()
        r = requests.get(f"{BaseUrl_1}/api/mer/cooperative/merchant/queryPage")
        # 检查状态码
        self.assertEqual(r.status_code, 200)

    def test_Afpn_003_2(self):
        """
        合作-部门列表
        """
        s = Steps().open(f"{BaseUrl_1}/cooperation/cooperation/department")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/mer/department/queryPage",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_003_3(self):
        """
        合作-职务列表
        """
        s = Steps().open(f"{BaseUrl_1}/cooperation/cooperation/position")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/mer/position/queryPage",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_003_4(self):
        """
        合作-企业员工
        """
        s = Steps().open(f"{BaseUrl_1}/cooperation/cooperation/employee")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/us/employee/query/page",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_003_5(self):
        """
        合作-员工分组
        """
        s = Steps().open(f"{BaseUrl_1}/cooperation/cooperation/companyEmployeeGroup")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/mer/employee/group/queryPage",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_004_1(self):
        """
        订单-订单列表
        """
        s = Steps().open(f"{BaseUrl_1}/order/order/offline")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/order/queryPage",
            json={
                "merchantId": "2021040701",
                "cooperativeMerchantCode": None,
                "sysId": "iom",
                "departmentIdList": [],
                "positionIdList": [],
                "storeIds": [],
                "departId": None,
                "queryTimeType": 0,
                "orderStatusList": ["2", "3", "6", "9", "10"],
                "orderOriginalList": ["3", "4", "5", "6", "10", "11"],
                "orderType": 1,
                "refundStatus": None,
                "createTime": None,
                "startDate": "2024-11-19T16:00:00.000Z",
                "endDate": "2024-11-20T15:59:59.999Z",
                "mealType": None,
                "pageNum": 1,
                "delFlag": 0,
                "pageSize": 10,
                "reserveStatusList": [],
                "foodCard": None,
            },
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_004_2(self):
        """
        订单-退款列表
        """
        s = Steps().open(f"{BaseUrl_1}/order/audit/refund")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/ts/applyRefund/queryPage",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_004_3(self):
        """
        订单-投取餐管理
        """
        s = Steps().open(f"{BaseUrl_1}/order/feedtakemeals/feedtakemeals")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/ts/applyRefund/queryPage",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_004_4(self):
        """
        订单-配送单管理
        """
        s = Steps().open(f"{BaseUrl_1}/order/delivery/order")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/ts/orderDelivery/queryPage",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_004_5(self):
        """
        订单-备取餐管理
        """
        s = Steps().open(f"{BaseUrl_1}/order/delivery/prepareMeal")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/ts/orderDelivery/queryPage",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_004_6(self):
        """
        订单-评价概览
        """
        s = Steps().open(f"{BaseUrl_1}/order/evaluate/situation")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/evaluation/profile/queryPage",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_004_7(self):
        """
        订单-评价内容
        """
        s = Steps().open(f"{BaseUrl_1}/order/evaluate/content")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/evaluation/content/queryPage",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_005_1(self):
        """
        财务-用户流水
        """
        s = Steps().open(f"{BaseUrl_1}/financial/flow/userflow")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/ts/orderRecord/queryPage",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_005_2(self):
        """
        财务-商户对账
        """
        s = Steps().open(f"{BaseUrl_1}/financial/reconciliation/merchant")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/ts/businessCheck/page",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_005_3(self):
        """
        财务-档口对账
        """
        s = Steps().open(f"{BaseUrl_1}/financial/reconciliation/store")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/ts/businessCheck/page",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_005_4(self):
        """
        财务-合作商消费对账
        """
        s = Steps().open(f"{BaseUrl_1}/financial/reconciliation/partner")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/ts/businessCheck/enterprise/page",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_005_5(self):
        """
        财务-补贴下发扣除对账
        """
        s = Steps().open(f"{BaseUrl_1}/financial/reconciliation/subsidyDeduction")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/ts/subsidyCheck/queryPage",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_005_6(self):
        """
        财务-企业员工对账
        """
        s = Steps().open(f"{BaseUrl_1}/financial/reconciliation/self")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/ts/cooperate/consume/queryPage",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_005_7(self):
        """
        财务-减免次数统计
        """
        s = Steps().open(f"{BaseUrl_1}/financial/reconciliation/reducecount")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/employee/derate/summary",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_005_8(self):
        """
        财务-商城对账
        """
        s = Steps().open(f"{BaseUrl_1}/financial/reconciliation/shop")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/ts/busines/shop/queryExtMerchantCheckPage",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_005_9(self):
        """
        财务-渠道收款统计
        """
        s = Steps().open(f"{BaseUrl_1}/financial/reconciliation/channelcollection")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/query/dwdPayChannelAmountD/page",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_006_1(self):
        """
        菜品-规格
        """
        s = Steps().open(f"{BaseUrl_1}/dishes/attribute/spec")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/goods/specgroup/queryPage",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_006_2(self):
        """
        菜品-口味
        """
        s = Steps().open(f"{BaseUrl_1}/dishes/attribute/flavor")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/goods/flavorgroup/queryPage",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_006_3(self):
        """
        菜品-分类
        """
        s = Steps().open(f"{BaseUrl_1}/dishes/attribute/category")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/goods/category/queryPage",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_006_4(self):
        """
        菜品-单品菜品
        """
        s = Steps().open(f"{BaseUrl_1}/dishes/dish/single")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/goods/dish/queryPage",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_006_5(self):
        """
        菜品-单品组合
        """
        s = Steps().open(f"{BaseUrl_1}/dishes/dish/singlecomb")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/goods/dish/group/queryAll",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_006_6(self):
        """
        菜品-套餐菜品
        """
        s = Steps().open(f"{BaseUrl_1}/dishes/dish/combo")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/goods/combo/queryPage",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_006_7(self):
        """
        菜品-菜品备注
        """
        s = Steps().open(f"{BaseUrl_1}/dishes/dish/remark")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/goods/food/remark/queryPage",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_006_8(self):
        """
        菜品-排餐
        """
        s = Steps().open(f"{BaseUrl_1}/dishes/dish/arrange")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/goods/food/remark/queryPage",
            json={
                "pageNum": 1,
                "pageSize": 10,
                "delFlag": 0,
                "storeId": "1fda7cedd736452fb5ea6f2f1f3eae36",
                "merchantId": "2021040701",
                "startDate": "2024-11-18",
                "foodName": "",
                "valuationType": 3,
            },
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_006_9(self):
        """
        菜品-食材预估
        """
        s = Steps().open(f"{BaseUrl_1}/dishes/dish/ingredientEstimate")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/mer/estimation/queryPage",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_006_10(self):
        """
        菜品-菜谱分组
        """
        s = Steps().open(f"{BaseUrl_1}/dishes/kitchen/group")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/stir/recipe/group/queryPage",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_006_11(self):
        """
        菜品-菜谱分类
        """
        s = Steps().open(f"{BaseUrl_1}/dishes/kitchen/typerecipe")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/stir/recipe/type/queryPage",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_006_12(self):
        """
        菜品-原料管理
        """
        s = Steps().open(f"{BaseUrl_1}/dishes/kitchen/material")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/stir/ingredients/queryPage",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_006_13(self):
        """
        菜品-调料管理
        """
        s = Steps().open(f"{BaseUrl_1}/dishes/kitchen/flavour")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/stir/seasoning/queryPage",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_006_14(self):
        """
        菜品-平台菜谱
        """
        s = Steps().open(f"{BaseUrl_1}/dishes/kitchen/platformMenu")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/stir/recipe/base/queryRecipeBasePage",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_006_15(self):
        """
        菜品-自研菜谱
        """
        s = Steps().open(f"{BaseUrl_1}/dishes/kitchen/selfstudyMenu")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/stir/recipe/base/queryRecipeBasePage",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_006_16(self):
        """
        菜品-菜谱授权
        """
        s = Steps().open(f"{BaseUrl_1}/dishes/kitchen/menuLicense")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/stir/recipe/base/queryRecipeBasePage",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_006_17(self):
        """
        菜品-烧录分组
        """
        s = Steps().open(f"{BaseUrl_1}/dishes/kitchen/divideburn")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/stir/burn/group/queryPage",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_006_18(self):
        """
        菜品-菜谱下发
        """
        s = Steps().open(f"{BaseUrl_1}/dishes/kitchen/issue")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/stir/recipe/burnbase/queryPage",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_007_1(self):
        """
        运营-提现管理
        """
        s = Steps().open(f"{BaseUrl_1}/operate/business/withdraw")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/ts/withDrawl/queryPage",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_007_2(self):
        """
        运营-补贴下发
        """
        s = Steps().open(f"{BaseUrl_1}/operate/business/subsidyallot")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/ts/subsidy/queryPageExample",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_007_3(self):
        """
        运营-补贴扣除
        """
        s = Steps().open(f"{BaseUrl_1}/operate/business/subsidydeduct")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/ts/subsidyDeduct/queryPage",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_007_4(self):
        """
        运营-补贴规则
        """
        s = Steps().open(f"{BaseUrl_1}/operate/business/subsidyrules")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/subsidy/querySubsidyPage",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_007_5(self):
        """
        运营-减免规则
        """
        s = Steps().open(f"{BaseUrl_1}/operate/business/deductrules")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/ts/quotaconfig/queryPage",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_007_6(self):
        """
        运营-绑盘限制
        """
        s = Steps().open(f"{BaseUrl_1}/operate/business/bindlimit")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/ts/bindTrayRule/queryPage",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_007_7(self):
        """
        运营-预定管理
        """
        s = Steps().open(f"{BaseUrl_1}/operate/business/reservation")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/mer/store/queryPageExample/two",
        )
        self.assertEqual(r.status_code, 200)
    

    def test_Afpn_007_8(self):
        """
        运营-充值福利
        """
        s = Steps().open(f"{BaseUrl_1}/operate/sales/rechargewelfare")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/ts/welfare/queryPageExample",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_007_9(self):
        """
        运营-消费次数
        """
        s = Steps().open(f"{BaseUrl_1}/operate/sales/consumetimes")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/mer/consumption/times/queryPage",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_007_10(self):
        """
        运营-线下餐券
        """
        s = Steps().open(f"{BaseUrl_1}/operate/sales/offlinetickets")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/mer/mealticket/queryPage",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_007_11(self):
        """
        运营-优惠活动
        """
        s = Steps().open(f"{BaseUrl_1}/operate/sales/specialoffer")
        s.sleep()
        self.assertStatusOk()
        r = requests.get(
            f"{BaseUrl_1}/api/activity/performActivityList",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_007_12(self):
        """
        运营-优惠活动统计
        """
        s = Steps().open(f"{BaseUrl_1}/operate/sales/specialactivitieStatistics")
        s.sleep()
        self.assertStatusOk()
        r = requests.get(
            f"{BaseUrl_1}/api/activity/getActivityOrderStat",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_007_13(self):
        """
        运营-报餐管理
        """
        s = Steps().open(f"{BaseUrl_1}/operate/otmeal/mealManage")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/ts/mealEnroll/queryPage",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_007_14(self):
        """
        运营-核销记录
        """
        s = Steps().open(f"{BaseUrl_1}/operate/otmeal/verificationRecord")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/ts/mealEnrollUse/queryPage",
        )
        self.assertEqual(r.status_code, 200)
        

    def test_Afpn_008_1(self):
        """
        食安-健康证
        """
        s = Steps().open(f"{BaseUrl_1}/foodsafety/health/health")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/mer/healthCert/queryPage",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_008_2(self):
        """
        食安-岗位管理
        """
        s = Steps().open(f"{BaseUrl_1}/foodsafety/health/post")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/mer/healthPost/queryPage",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_009_1(self):
        """
        服务-软件服务概览
        """
        s = Steps().open(f"{BaseUrl_1}/service/softwareService/serviceCondition")
        s.sleep()
        self.assertStatusOk()
        r = requests.get(
            f"{BaseUrl_1}/api/sales/mer/si/findByMerchantId",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_009_2(self):
        """
        服务-短信服务概览
        """
        s = Steps().open(f"{BaseUrl_1}/service/messageService/smsOverView")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/sales/mer/rpi/getSmsAvailableCount",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_009_3(self):
        """
        服务-短信记录
        """
        s = Steps().open(f"{BaseUrl_1}/service/messageService/smsRecord")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/mer/sms/send/record/queryPage",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_009_4(self):
        """
        服务-账户概览
        """
        s = Steps().open(f"{BaseUrl_1}/service/expenseManage/accountInfo")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/sales/mer/account/geAccountList",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_009_5(self):
        """
        服务-收支明细
        """
        s = Steps().open(f"{BaseUrl_1}/service/expenseManage/incomeExpendDetail")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/sales/mer/cashFlow/getCashFlowList",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_009_6(self):
        """
        服务-转账管理
        """
        s = Steps().open(f"{BaseUrl_1}/service/expenseManage/transfersManage")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/mer/trade/offline/queryPage",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_009_7(self):
        """
        服务-订单管理
        """
        s = Steps().open(f"{BaseUrl_1}/service/expenseManage/orderManage")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/sales/mer/serviceOrder/getOrderList",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_009_8(self):
        """
        服务-发票管理
        """
        s = Steps().open(f"{BaseUrl_1}/service/expenseManage/ticketManage")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/mer/invoice/request/queryPage",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_009_9(self):
        """
        服务-发票抬头
        """
        s = Steps().open(f"{BaseUrl_1}/service/expenseManage/ticketTitle")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/mer/invoice/title/queryPage",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_010_1(self):
        """
        数据-菜品销售统计
        """
        s = Steps().open(f"{BaseUrl_1}/data/statistics/dishsale")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/orderdetail/ts/orderDetail/dishAggPage",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_010_2(self):
        """
        数据-菜品退款统计
        """
        s = Steps().open(f"{BaseUrl_1}/data/statistics/dishrefund")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/orderdetail/ts/orderDetail/dishAggPage",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_010_3(self):
        """
        数据-菜品汇总统计
        """
        s = Steps().open(f"{BaseUrl_1}/data/statistics/dishsum")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/order/dish/agg/findCollectList",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_010_4(self):
        """
        数据-预定取餐统计
        """
        s = Steps().open(f"{BaseUrl_1}/data/statistics/dishpickup")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/reserve/dishAgg/queryPage",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_010_5(self):
        """
        数据-炒菜机烹饪数据
        """
        s = Steps().open(f"{BaseUrl_1}/data/statistics/cooking")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/stir/menu/burn/record/queryPage",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_010_6(self):
        """
        数据-炒菜机运行数据
        """
        s = Steps().open(f"{BaseUrl_1}/data/statistics/running")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/stir/merchant/burn/recipe/queryPage",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_010_7(self):
        """
        数据-蒸烤箱烹饪数据
        """
        s = Steps().open(f"{BaseUrl_1}/data/statistics/roastcooking")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/stir/menu/burn/record/queryPage",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_010_8(self):
        """
        数据-蒸烤箱运行数据
        """
        s = Steps().open(f"{BaseUrl_1}/data/statistics/roastrunning")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/stir/roast/cook/record/queryPage",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_010_9(self):
        """
        数据-消费数据分析
        """
        s = Steps().open(f"{BaseUrl_1}/data/statistics/consumedataana")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/orderdetail/ts/consumption/data/analysis",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_010_10(self):
        """
        数据-行为数据
        """
        s = Steps().open(f"{BaseUrl_1}/data/statistics/behavioraldata")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/mer/camera/queryWarningPage",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_010_11(self):
        """
        数据-称重机菜品
        """
        s = Steps().open(f"{BaseUrl_1}/data/statistics/weighingmachinerecipe")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/mer/machinegoodconfig/queryMachineGoodPage",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_010_12(self):
        """
        数据-智慧经营大数据
        """
        s = Steps().open(f"{BaseUrl_1}/data/bigscreen/businessbigdata")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/dw/app/data/iom/bulk",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_010_13(self):
        """
        数据-前厅数据可视化
        """
        s = Steps().open(f"{BaseUrl_1}/data/bigscreen/lobbyData")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/dw/app/data/iom/bulk",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_010_14(self):
        """
        数据-采购数据可视化
        """
        s = Steps().open(f"{BaseUrl_1}/data/bigscreen/purchaseData")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/dw/app/data/iom/bulk",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_010_15(self):
        """
        数据-智慧后厨可视化
        """
        s = Steps().open(f"{BaseUrl_1}/data/bigscreen/smartkitchen")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/dw/app/data/iom/bulk",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_010_16(self):
        """
        数据-菜品余量看板
        """
        s = Steps().open(f"{BaseUrl_1}/data/bigscreen/marginsignage")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/dw/app/data/iom/bulk",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_010_17(self):
        """
        数据-导入文件
        """
        s = Steps().open(f"{BaseUrl_1}/data/importAndExport/importfile")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/import/query",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_010_18(self):
        """
        数据-导出文件
        """
        s = Steps().open(f"{BaseUrl_1}/data/importAndExport/exportfile")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/export/query",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_011_1(self):
        """
        运维-账号管理
        """
        s = Steps().open(f"{BaseUrl_1}/maintenance/safe/account")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/uims/user/queryPage",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_011_2(self):
        """
        运维-角色管理
        """
        s = Steps().open(f"{BaseUrl_1}/maintenance/safe/role")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/uims/role/queryPage",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_011_3(self):
        """
        运维-管理员卡
        """
        s = Steps().open(f"{BaseUrl_1}/maintenance/safe/admincard")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/mer/machinemanagementcard/query/example",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_011_4(self):
        """
        运维-档口分组
        """
        s = Steps().open(f"{BaseUrl_1}/maintenance/store/group")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/mer/tree/group/next/one",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_011_5(self):
        """
        运维-档口列表
        """
        s = Steps().open(f"{BaseUrl_1}/maintenance/store/list")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/mer/store/queryPageExample/two",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_011_6(self):
        """
        运维-设备管理
        """
        s = Steps().open(f"{BaseUrl_1}/maintenance/maintain/equipment")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/mer/machine/queryPageExampleList",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_011_7(self):
        """
        运维-托盘管理
        """
        s = Steps().open(f"{BaseUrl_1}/maintenance/maintain/tray")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/mer/repast/queryPageExample",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_011_8(self):
        """
        运维-打印机管理
        """
        s = Steps().open(f"{BaseUrl_1}/maintenance/maintain/printer")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/mer/machineprint/queryPage",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_011_9(self):
        """
        运维-配送员管理
        """
        s = Steps().open(f"{BaseUrl_1}/maintenance/deliverer/deliverer")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/mer/orderDeliverer/queryPage",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_011_10(self):
        """
        运维-就餐区域
        """
        s = Steps().open(f"{BaseUrl_1}/maintenance/location/diningArea")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/mer/merMerchantArea/queryPage",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_011_11(self):
        """
        运维-就餐位置
        """
        s = Steps().open(f"{BaseUrl_1}/maintenance/location/diningLocation")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/mer/merchant/area/location/queryPage",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_012_1(self):
        """
        系统-设置
        """
        s = Steps().open(f"{BaseUrl_1}/system/settings/settings")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/mer/merchant/area/location/queryPage",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_012_2(self):
        """
        系统-登录日志
        """
        s = Steps().open(f"{BaseUrl_1}/system/logManage/loginLog")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/oplog/queryPage",
        )
        self.assertEqual(r.status_code, 200)

    def test_Afpn_012_3(self):
        """
        系统-操作日志
        """
        s = Steps().open(f"{BaseUrl_1}/system/logManage/operateLog")
        s.sleep()
        self.assertStatusOk()
        r = requests.post(
            f"{BaseUrl_1}/api/oplog/queryPage",
        )
        self.assertEqual(r.status_code, 200)


# my_object = AfpnTest()  # 假设MyClass是一个类，my_object是它的一个实例
# attributes = dir(my_object)
# print(attributes)

# attributes = vars(my_object)
# print(attributes)

# instance_attributes = my_object.__dict__
# print(instance_attributes)


# 增加浏览器代理示例
if __name__ == "__main__":
    # proxy = "127.0.0.1:1080"  # 示例代理地址和端口

    # chrome_options = ChromeOptions()
    # chrome_options.add_argument(f"--proxy-server={proxy}")
    # browser = {
    #     "browser": "chrome",
    #     "options": chrome_options,
    # }
    seldom.main(
        case="test_apfn_4.AfpnTest",
        # browser=browser
        browser="gc",
        # browser="firefox",
        tester="tzk",
        description="数字餐厅",
        # debug=True,
    )
