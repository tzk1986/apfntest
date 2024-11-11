import seldom
from seldom import Steps

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
        s.sleep(3)
        pass

    def test_Afpn_1_2(self):
        """
        基础数据-供应商
        """
        s = Steps()
        s.open(f"{BaseUrl}/basicData/supplierList")
        s.sleep(3)
        pass

    def test_Afpn_1_3(self):
        """
        基础数据-商户配置
        """
        s = Steps()
        s.open(f"{BaseUrl}/basicData/merchant")
        s.sleep(3)
        pass

    def test_Afpn_1_4(self):
        """
        基础数据-档口配置
        """
        s = Steps()
        s.open(f"{BaseUrl}/basicData/store")
        s.sleep(3)
        pass

    def test_Afpn_1_5(self):
        """
        基础数据-账号管理
        """
        s = Steps()
        s.open(f"{BaseUrl}/basicData/accountManage")
        s.sleep(3)
        pass

    def test_Afpn_2_1(self):
        """
        物料管理-物料分类
        """
        s = Steps()
        s.open(f"{BaseUrl}/materialManage/MaterialCategory")
        s.sleep(3)
        pass

    def test_Afpn_2_2(self):
        """
        物料管理-物料品牌
        """
        s = Steps()
        s.open(f"{BaseUrl}/materialManage/materialBrand")
        s.sleep(3)
        pass

    def test_Afpn_2_3(self):
        """
        物料管理-SPU管理
        """
        s = Steps()
        s.open(f"{BaseUrl}/materialManage/spuManage")
        s.sleep(3)
        pass

    def test_Afpn_2_4(self):
        """
        物料管理-物料档案
        """
        s = Steps()
        s.open(f"{BaseUrl}/materialManage/materialRecord")
        s.sleep(3)
        pass

    def test_Afpn_2_5(self):
        """
        物料管理-货源管理
        """
        s = Steps()
        s.open(f"{BaseUrl}/materialManage/sourceManage")
        s.sleep(3)
        pass

    def test_Afpn_2_6(self):
        """
        物料管理-直送物料
        """
        s = Steps()
        s.open(f"{BaseUrl}/materialManage/directSendMaterial")
        s.sleep(3)
        pass

    def test_Afpn_2_7(self):
        """
        物料管理-常用物料
        """
        s = Steps()
        s.open(f"{BaseUrl}/materialManage/commonUseMaterial")
        s.sleep(3)
        pass

    def test_Afpn_3_1(self):
        """
        价格管理-采购价格
        """
        s = Steps()
        s.open(f"{BaseUrl}/priceManage/purchasePrice")
        s.sleep(3)
        pass

    def test_Afpn_3_2(self):
        """
        价格管理-出库价格
        """
        s = Steps()
        s.open(f"{BaseUrl}/priceManage/retrievalPrice")
        s.sleep(3)
        pass

    def test_Afpn_3_3(self):
        """
        价格管理-调价管理
        """
        s = Steps()
        s.open(f"{BaseUrl}/priceManage/adjustPrice")
        s.sleep(3)
        pass

    def test_Afpn_4_1(self):
        """
        采购管理-物料申请单
        """
        s = Steps()
        s.open(f"{BaseUrl}/purchaseManage/materialApplication")
        s.sleep(3)
        pass
    
    def test_Afpn_4_2(self):
        """
        采购管理-竞价采购
        """
        s = Steps()
        s.open(f"{BaseUrl}/purchaseManage/competition")
        s.sleep(3)
        pass

    def test_Afpn_4_3(self):
        """
        采购管理-报价采购
        """
        s = Steps()
        s.open(f"{BaseUrl}/purchaseManage/quotation")
        s.sleep(3)
        pass

    def test_Afpn_4_4(self):
        """
        采购管理-采购订单
        """
        s = Steps()
        s.open(f"{BaseUrl}/purchaseManage/purchaseOrder")
        s.sleep(3)
        pass

    def test_Afpn_4_5(self):
        """
        采购管理-结算主体
        """
        s = Steps()
        s.open(f"{BaseUrl}/purchaseManage/purchasePrincipal")
        s.sleep(3)
        pass

    def test_Afpn_5_1(self):
        """
        库存管理-验收管理
        """
        s = Steps()
        s.open(f"{BaseUrl}/stockManage/inboundAcceptance")
        s.sleep(3)
        pass

    def test_Afpn_5_2(self):
        """
        库存管理-领用管理
        """
        s = Steps()
        s.open(f"{BaseUrl}/stockManage/outboundPickOut")
        s.sleep(3)
        pass

    def test_Afpn_5_3(self):
        """
        库存管理-入库单
        """
        s = Steps()
        s.open(f"{BaseUrl}/stockManage/inboundReceipt")
        s.sleep(3)
        pass

    def test_Afpn_5_4(self):
        """
        库存管理-出库单
        """
        s = Steps()
        s.open(f"{BaseUrl}/stockManage/outboundReceipt")
        s.sleep(3)
        pass

    def test_Afpn_5_5(self):
        """
        库存管理-库存查询
        """
        s = Steps()
        s.open(f"{BaseUrl}/stockManage/stockSearch")
        s.sleep(3)
        pass

    def test_Afpn_5_6(self):
        """
        库存管理-库存流水查询
        """
        s = Steps()
        s.open(f"{BaseUrl}/stockManage/stockJournalizing")
        s.sleep(3)
        pass

    def test_Afpn_5_7(self):
        """
        库存管理-预警配置
        """
        s = Steps()
        s.open(f"{BaseUrl}/stockManage/alertConfig")
        s.sleep(3)
        pass

    def test_Afpn_5_8(self):
        """
        库存管理-仓库
        """
        s = Steps()
        s.open(f"{BaseUrl}/stockManage/wareHouse")
        s.sleep(3)
        pass

    def test_Afpn_5_9(self):
        """
        库存管理-配送点
        """
        s = Steps()
        s.open(f"{BaseUrl}/stockManage/distributionSite")
        s.sleep(3)
        pass

    def test_Afpn_6_1(self):
        """
        财务管理-供应商对账
        """
        s = Steps()
        s.open(f"{BaseUrl}/financeManage/supplierReconciliation")
        s.sleep(3)
        pass

    def test_Afpn_6_2(self):
        """
        财务管理-验收统计
        """
        s = Steps()
        s.open(f"{BaseUrl}/financeManage/acceptanceStatistics")
        s.sleep(3)
        pass

    def test_Afpn_6_3(self):
        """
        财务管理-档口对账
        """
        s = Steps()
        s.open(f"{BaseUrl}/financeManage/storeReconciliation")
        s.sleep(3)
        pass

    def test_Afpn_7_1(self):
        """
        数据报表-档口领用统计
        """
        s = Steps()
        s.open(f"{BaseUrl}/dataReport/storeReceiveStatistics")
        s.sleep(3)
        pass

    def test_Afpn_8_1(self):
        """
        导入导出-导入管理
        """
        s = Steps()
        s.open(f"{BaseUrl}/dataCenter/importedFiles")
        s.sleep(3)
        pass

    def test_Afpn_8_2(self):
        """
        导入导出-导出管理
        """
        s = Steps()
        s.open(f"{BaseUrl}/dataCenter/exportedFiles")
        s.sleep(3)
        pass


if __name__ == '__main__':
    seldom.main(
                case='test_apfn_3.AfpnTest', 
                browser="gc", 
                # browser="firefox",
                tester="tzk",
                debug=True
                )