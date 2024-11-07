import seldom
from seldom import Steps

# 测试环境 数字餐厅管理端
BaseUrl = "http://10.50.11.120:9002"

# 预发布环境
# BaseUrl = "https://toc.epfly.com.cn/"


class AfpnTest(seldom.TestCase):
    """
    数字餐厅 经营管理
    """

    def start(self):

        print("开始测试")

    def end(self):
        print("结束测试")

    def test_Afpn_0_1(self):
        """
        登录
        """
        print(f"{BaseUrl}/login")
        s = Steps().open(f"{BaseUrl}/login")
        
        
        s.find('#app > div > form > div:nth-child(2) > div > div > input').type("18335161013")
        s.find('#app > div > form > div:nth-child(3) > div > div > input').type("112233")
        s.find('#app > div > form > div:nth-child(4) > div > div > div.login-input-code.el-input.el-input--prefix > input').type("1")
        s.find('#app > div > form > div:nth-child(5) > div > button').click()
        s.sleep(1)
        self.get_cookies()
        print(self.get_cookies())
        

    def test_Afpn_2_1(self):
        """
        入驻-总部
        """
        s = Steps().open(f"{BaseUrl}/storeEnter/settlein/head")
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div.search_option_left.s-gap-6-15 > div:nth-child(1) > div > input')
        s.type("服务费测试总部")
        # 点击查询
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div.search_option_left.s-gap-6-15 > div.s-gap-6-10.s-g-l-0 > button').click()
        

    def test_Afpn_2_2(self):
        """
        入驻-业主
        """
        s = Steps().open(f"{BaseUrl}/storeEnter/settlein/owner")
        self.assertText("入驻管理")
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div.search_option_left.s-gap-6-15 > div:nth-child(1) > div > input')
        s.type(text="测试业主")
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div.search_option_left.s-gap-6-15 > div.s-gap-6-10.s-g-l-0 > button').click()


    def test_Afpn_3_1(self):
        """
        商户-商户列表
        """
        s = Steps().open(f"{BaseUrl}/merchant/merchantList")
        self.assertText("商户管理")       
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div.search_option_left.s-gap-6-15 > div:nth-child(1) > div > div > input').click()
        s.sleep(1)
        s.find('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(80)').click()
        s.sleep(1)
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div.search_option_left.s-gap-6-15 > div:nth-child(2) > div > input')
        s.type(text="艾佩")
        self.assertText("上海艾佩菲宁")
  
    def test_Afpn_3_2(self):
        """
        商户-档口列表
        """
        s = Steps().open(f"{BaseUrl}/merchant/storeList")
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div > div:nth-child(1) > div > input')
        s.type("上海艾佩菲宁互联网科技有限公司")
        self.assertText("档口列表")
        s.sleep(1)

    def test_Afpn_4_1(self):
        """ 
        会员-平台会员
        """
        s = Steps().open(f"{BaseUrl}/vip/platformVip")
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div > div:nth-child(1) > div > input')
        s.type("15900506254")
        # self.assertText("测试tzk")


    def test_Afpn_4_2(self):
        """
        会员-商户会员
        """
        s = Steps().open(f"{BaseUrl}/vip/merchantVip")
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div > div:nth-child(1) > div.common_input.el-input.el-input--suffix > input')
        s.type("上海艾佩菲宁")
        s.sleep(1)
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div > div:nth-child(2) > div > div > div > div > input').click()
        s.sleep(1)
        # 不能直接使用chrome浏览器获取,是动态的css,需要人为确定在第几个位置,然后点击
        s.find('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(2)').click()
        s.sleep(1)
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div > div:nth-child(2) > div > input')
        s.type("艾佩")
        s.sleep(1)

    def test_Afpn_4_3(self):
        """
        会员-员工列表
        """
        s = Steps().open(f"{BaseUrl}/vip/employees")
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div.search_option_left.s-gap-6-15 > div:nth-child(1) > div > div.el-input.el-input--suffix > input').click()
        s.sleep(1)
        s.find('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(126)').click()
        s.sleep(1)
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div.search_option_left.s-gap-6-15 > div:nth-child(3) > div > input')
        s.type("15900909029")
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div.search_option_left.s-gap-6-15 > div.s-gap-6-10.s-g-l-0 > button > span').click()
        s.sleep(1)

        
    def test_Afpn_5_1(self):
        """
        服务-实例管理
        """
        s = Steps().open(f"{BaseUrl}/service/instanceManage")
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div > div:nth-child(1) > div > div > input').click()
        # 商户名称选择上海艾佩菲宁搜索
        s.find('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1)').click()
        s.sleep(1)


    def test_Afpn_5_2(self):
        """
        服务-短信记录
        """
        s = Steps().open(f"{BaseUrl}/service/smsRecord")
        s.sleep(1)
        

    def test_Afpn_5_3(self):
        """
        服务-账户管理
        """
        s = Steps().open(f"{BaseUrl}/service/accountManage")
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div > div:nth-child(1) > div > div > input').click()
        # 商户名称选择上海艾佩菲宁搜索
        s.find('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1) > span').click()
        self.sleep(1)

    def test_Afpn_5_4(self):
        """
        服务-收支明细
        """
        s = Steps().open(f"{BaseUrl}/service/incomeExpendDetail")

        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div.search_option_left.s-gap-6-15 > div:nth-child(5) > div > div.el-input.el-input--suffix > input').click()
        s.sleep(1)
        # 选择交易方式，查看结果
        s.find('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1)').click()
        s.sleep(1)
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div.search_option_left.s-gap-6-15 > div:nth-child(5) > div > div > input').click()
        s.sleep(1)
        s.find('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(3)').click()
        s.sleep(1)
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div.search_option_left.s-gap-6-15 > div:nth-child(5) > div > div > input').click()
        s.sleep(1)
        s.find('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(2)').click()
        s.sleep(1)
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div.search_option_left.s-gap-6-15 > div:nth-child(5) > div > div > input')
        # 模拟鼠标移动到元素上，显示为清空“叉”按钮
        s.move_to_element()
        # 找到对应的可点击范围，点击清空
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div.search_option_left.s-gap-6-15 > div:nth-child(5) > div > div > span > span ').click()
        s.sleep(1)

        

    def test_Afpn_5_5(self):
        """
        服务-转账管理
        """
        s = Steps().open(f"{BaseUrl}/service/transferManage")
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div > div:nth-child(1) > div > div > input')
        s.type("上海艾佩菲宁")

        # 商户名称选择上海艾佩菲宁搜索
        s.find('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:last-child').click()
        s.sleep(1)
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div > div:nth-child(2) > div > div > input').click()
        s.sleep(1)
        s.find('body > div:nth-child(6) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1)').click()
        s.sleep(1)
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div > div:nth-child(2) > div > div > input').click()
        s.sleep(1)
        s.find('body > div:nth-child(6) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(2)').click()
        s.sleep(1)
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div > div:nth-child(2) > div > div > input').click()
        s.sleep(1)
        s.find('body > div:nth-child(6) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(3)').click()
        s.sleep(1)
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div > div:nth-child(2) > div > div > input')
        s.move_to_element()
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div > div:nth-child(2) > div > div > span > span').click()
        s.sleep(1)
        

    def test_Afpn_5_6(self):
        """
        服务-订单管理
        """
        s = Steps().open(f"{BaseUrl}/service/orderManage")
        # 商户名称 
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div > div:nth-child(1) > div > div > input').click()
        # 商户名称选择上海艾佩菲宁搜索
        s.find('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1)').click()
        s.sleep(1)
        # 支付状态
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div > div:nth-child(3) > div > div.el-select__tags > input').click()
        s.sleep(1)
        # 选择未支付
        s.find('body > div.el-select-dropdown.el-popper.is-multiple > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1)').click()
        s.sleep(1)
        # 选择已支付
        s.find('body > div.el-select-dropdown.el-popper.is-multiple > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(2)').click()
        s.sleep(1)
        # 开票状态
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div > div:nth-child(4) > div > div.el-select__tags > input').click()
        s.sleep(1)
        # 选择未开票
        s.find('body > div:nth-child(7) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1)').click()
        s.sleep(1)
        # 订单类型
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div > div:nth-child(5) > div > div.el-select__tags > input').click()
        s.sleep(1)
        # 选择资源包
        s.find('body > div:nth-child(8) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(2)').click()
        s.sleep(1)
        # 选择软件服务
        s.find('body > div:nth-child(8) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1)').click()
        s.sleep(1)
        

    def test_Afpn_5_7(self):
        """
        服务-发票管理
        """
        s = Steps().open(f"{BaseUrl}/service/ticketManage")
        # 商户名称
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div > div:nth-child(1) > div > div.el-input.el-input--suffix > input').click()
        s.sleep(1)
        # 商户名称选择上海艾佩菲宁搜索
        s.find('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(126)').click()
        s.sleep(1)
        # 鼠标移动到申请开票时间
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div > div:nth-child(2) > div')
        s.move_to_element()
        s.sleep(1)
        # 点击清空
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div > div:nth-child(2) > div > i.el-input__icon.el-range__close-icon').click()
        s.sleep(1)

    def test_Afpn_6_1(self):
        """
        业务-补贴下发
        """
        s = Steps().open(f"{BaseUrl}/business/subsidyIssue")
        # 创建商户/合作商
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div > div:nth-child(1) > div > input')
        s.type("上海艾佩菲宁")
        # 生效状态
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div > div:nth-child(3) > div > div > input').click()
        s.sleep(1)
        # 生效中
        s.find('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(2)').click()
        # 鼠标移动到生效状态
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div > div:nth-child(3) > div > div > input')
        s.move_to_element()
        # 点击清空
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div > div:nth-child(3) > div > div > span > span ').click()
        s.sleep(1)

    def test_Afpn_6_2(self):
        """
        业务-充值福利
        """
        s = Steps().open(f"{BaseUrl}/business/welfare")
        # 商户名称
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div > div:nth-child(1) > div > div.el-input.el-input--suffix > input').click()
        s.sleep(1)
        s.find('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(126)').click()
        s.sleep(1)
        # 状态选择生效中
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div > div:nth-child(5) > div > div > input').click()
        s.sleep(1)
        s.find('body > div:nth-child(6) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(2)').click()      
        s.sleep(1)

    def test_Afpn_6_3(self):
        """
        业务-补贴扣除
        """
        s = Steps().open(f"{BaseUrl}/business/subsidyDeduct")
        # 创建商户/合作商
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div > div:nth-child(1) > div > input')
        s.type('上海艾佩菲宁')
        # 执行状态 选择未执行
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div > div:nth-child(4) > div > div > input').click()
        s.sleep(1)
        s.find('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(2)').click()
        s.sleep(1)

    def test_Afpn_6_4(self):
        """
        业务-补贴规则
        """
        s = Steps().open(f"{BaseUrl}/business/subsidyConfig")
        # 商户名称
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div > div:nth-child(1) > div > div.el-input.el-input--suffix > input').click()
        s.sleep(1)
        s.find('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(126)').click()
        s.sleep(1)
        # 状态选择生效中
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div > div:nth-child(4) > div > div.el-input.el-input--suffix > input').click()
        s.sleep(1)
        s.find('body > div:nth-child(6) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(2)').click()
        s.sleep(1)


    def test_Afpn_6_5(self):
        """
        业务-减免规则
        """
        s = Steps().open(f"{BaseUrl}/business/quotaConfig")
        # 商户名称
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div > div:nth-child(1) > div > div.el-input.el-input--suffix > input').click()
        s.sleep(1)
        s.find('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(126)').click()
        s.sleep(1)
        # 状态选择生效中
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div > div:nth-child(4) > div > div > input').click()
        s.sleep(1)
        s.find('body > div:nth-child(6) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(2)').click()
        s.sleep(1)

    def test_Afpn_6_6(self):
        """
        业务-充值消费
        """
        s = Steps().open(f"{BaseUrl}/business/chargeConsumeConfig")
        # 状态选择启用
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div > div:nth-child(2) > div > div > input').click()
        s.sleep(1)
        s.find('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(2)').click()
        s.sleep(1)
    
    def test_Afpn_6_7(self):
        """
        业务-消费次数
        """
        s = Steps().open(f"{BaseUrl}/business/consumptionTimes")
        # 状态选择启用
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div > div:nth-child(2) > div > div > input').click()
        s.sleep(1)
        s.find('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(2)').click()
        s.sleep(1)
        # 档口名称选择 美食美客
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div.search_option_left.s-gap-6-15 > div:nth-child(3) > div > div > input').click()
        s.sleep(1)
        s.find('body > div:nth-child(6) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:last-child').click()
        s.sleep(1)

    def test_Afpn_6_8(self):
        """
        业务-线下餐券
        """
        s = Steps().open(f"{BaseUrl}/business/mealTicket")
        # 商户名称
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div > div:nth-child(1) > div > div.el-input.el-input--suffix > input').click()
        s.sleep(1)
        s.find('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(126)').click()
        s.sleep(1)
        # 状态选择
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div > div:nth-child(4) > div > div > input').click()
        s.sleep(1)
        # 1未开始
        s.find('body > div:nth-child(6) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1)').click()
        s.sleep(1)
        # 状态选择
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div > div:nth-child(4) > div > div > input').click()
        s.sleep(1)
        # 2生效中
        s.find('body > div:nth-child(6) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(2)').click()
        s.sleep(1)
        # 状态选择
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div > div:nth-child(4) > div > div > input').click()
        s.sleep(1)
        # 3已过期
        s.find('body > div:nth-child(6) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(3)').click()
        s.sleep(1)
        # 状态选择
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div > div:nth-child(4) > div > div > input').click()
        s.sleep(1)
        # 4已作废
        s.find('body > div:nth-child(6) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(4)').click()
        s.sleep(1)

    def test_Afpn_6_9(self):
        """
        业务-餐券下发
        """
        s = Steps().open(f"{BaseUrl}/business/ticketIssue")
        # 发放状态
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div.search_option_left.s-gap-6-15 > div:nth-child(3) > div > div.el-input.el-input--suffix > input').click()
        s.sleep(1)
        # 发放中
        s.find('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(2)').click()
        s.sleep(1)
        # 发放状态
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div.search_option_left.s-gap-6-15 > div:nth-child(3) > div > div.el-input.el-input--suffix > input').click()
        s.sleep(1)
        # 已结束
        s.find('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(3)').click()
        s.sleep(1)

    def test_Afpn_7_1(self):
        """
        数据-数字餐厅驾驶舱
        """
        s = Steps().open(f"{BaseUrl}/data/digitalRestaurantCockpit")
        s.sleep(1)

    def test_Afpn_7_2(self):
        """
        数据-驾驶舱（参观）
        """
        s = Steps().open(f"{BaseUrl}/data/digitalRestaurantCockpiMask")
        s.sleep(1)

    def test_Afpn_7_3(self):
        """
        数据-叫号屏（参观）
        """
        s = Steps().open(f"{BaseUrl}/data/digitalCallScreen")
        s.sleep(1)

    def test_Afpn_8_1(self):
        """
        运维-托盘管理
        """
        s = Steps().open(f"{BaseUrl}/shop/traylist")
        # 选择托盘编号搜索
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div.search_option_left.s-gap-6-15 > div:nth-child(1) > div > div > div > div > input').click()
        s.sleep(1)
        s.find('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(3)').click()
        s.sleep(1)
        # 输入托盘编号123001471
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div.search_option_left.s-gap-6-15 > div:nth-child(1) > div > input')
        s.type('123001471')
        s.sleep(1)
        # 清空输入
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div.search_option_left.s-gap-6-15 > div:nth-child(1) > div > input')
        s.move_to_element()
        s.sleep(1)
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div.search_option_left.s-gap-6-15 > div:nth-child(1) > div > span').click()
        # 商户名称
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div.search_option_left.s-gap-6-15 > div:nth-child(2) > div > div > input').click()
        s.sleep(1)
        s.find('body > div:nth-child(6) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:last-child').click()
        s.sleep(1)
        # 档口名称 美食美克
        # s.refresh() # 为了能够不使用相同的css定位，刷新页面，直接获取定位值
        # body > div:nth-child(6) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(3)
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div.search_option_left.s-gap-6-15 > div:nth-child(3) > div > div > input').click()
        s.sleep(1)
        # 定位不到
        s.find('body > div:nth-child(7) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:last-child').click()
        s.sleep(1)
        # 绑盘方式 刷卡
        # s.refresh() # 为了能够不使用相同的css定位，刷新页面，直接获取定位值
        # body > div:nth-child(6) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(4)
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div.search_option_left.s-gap-6-15 > div:nth-child(4) > div > div > input').click()
        s.sleep(1)
        s.find('body > div:nth-child(8) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(2)').click()
        s.sleep(1)
        # 清空绑盘方式
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div.search_option_left.s-gap-6-15 > div:nth-child(4) > div > div > input')
        s.move_to_element()
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div.search_option_left.s-gap-6-15 > div:nth-child(4) > div > div > span > span').click()

        s.sleep(1)
        ### 递进查询每次css定位都会不一样，需要抓取定位时，真实模拟数据，查看定位信息


    def test_Afpn_8_1_1(self):
        """
        运维-托盘管理-托盘生成、托盘分配
        """
        s = Steps().open(f"{BaseUrl}/shop/traylist")
        # 点击托盘生成
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div.search_option_right.s-gap-6-10.s-g-l-0 > button:nth-child(1)').click()
        s.sleep(1)
        # 选择商户名称
        s.find('#app > section > section > section > main > section > section > main > div.main > div:nth-child(4) > div > div.el-dialog__body > div > div > form > div:nth-child(1) > div > div > div.el-input.el-input--suffix > input').click()
        s.sleep(1)
        s.find('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:last-child').click()
        s.sleep(1)
        # 托盘起始编号
        s.find('#app > section > section > section > main > section > section > main > div.main > div:nth-child(4) > div > div.el-dialog__body > div > div > form > div:nth-child(2) > div > div > input')
        s.type('1')
        # 托盘数量
        s.find('#app > section > section > section > main > section > section > main > div.main > div:nth-child(4) > div > div.el-dialog__body > div > div > form > div:nth-child(3) > div > div > input')
        s.type('1')
        # 点击确定
        s.find('#app > section > section > section > main > section > section > main > div.main > div:nth-child(4) > div > div.el-dialog__footer > div > button.el-button.common_button.el-button--primary > span').click()
        s.sleep(1)

        # 点击托盘分配
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div.search_option_right.s-gap-6-10.s-g-l-0 > button:nth-child(2) > span').click()
        s.sleep(1)
        # 选择商户名称
        s.find('#app > section > section > section > main > section > section > main > div.main > div:nth-child(5) > div > div.el-dialog__body > div > div > form > div:nth-child(1) > div > div > div > input').click()
        s.sleep(1)
        s.find('body > div:nth-child(7) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:last-child').click()
        s.sleep(1)
        # 选择档口
        s.find('#app > section > section > section > main > section > section > main > div.main > div:nth-child(5) > div > div.el-dialog__body > div > div > form > div:nth-child(2) > div > div > div > input').click()
        s.sleep(1)
        s.find('body > div:nth-child(8) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:last-child').click()
        s.sleep(1)
        # 托盘起始编号
        s.find('#app > section > section > section > main > section > section > main > div.main > div:nth-child(5) > div > div.el-dialog__body > div > div > form > div:nth-child(3) > div > div > input')
        s.type('0')
        # 托盘结束编号
        s.find('#app > section > section > section > main > section > section > main > div.main > div:nth-child(5) > div > div.el-dialog__body > div > div > form > div:nth-child(4) > div > div > input')
        s.type('1')
        # 点击确定
        s.find('#app > section > section > section > main > section > section > main > div.main > div:nth-child(5) > div > div.el-dialog__footer > div > button.el-button.common_button.el-button--primary > span').click()
        s.sleep(1)
        # 匹配确定
        s.find('#app > section > section > section > main > section > section > main > div.main > div.export_result_list > div.export_result_list_footer > button').click()
        s.sleep(1)

    def test_Afpn_8_2(self):
        """
        运维-管理员卡管理
        """
        s = Steps().open(f"{BaseUrl}/shop/idcard")
        # 手机号搜索
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div > div:nth-child(1) > div > input')
        s.type('15900506254')
        s.sleep(1)
        # 管理员卡号搜索
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div > div:nth-child(1) > div > div > div > div > input').click()
        s.sleep(1)
        s.find('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(3)').click()
        s.sleep(1)
        # 输入管理员卡号2681288190
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div > div:nth-child(1) > div > input')
        s.type('2681288190')
        s.sleep(1)
        # 商户名称搜索
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div > div:nth-child(2) > div > div.el-input.el-input--suffix > input').click()
        s.sleep(1)
        s.find('body > div:nth-child(6) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:last-child').click()
        s.sleep(1)
        # 档口查询
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div > div:nth-child(3) > div > div.el-input.el-input--suffix > input').click()
        s.sleep(1)
        s.find('body > div:nth-child(7) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:last-child').click()
        s.sleep(1)

    def test_Afpn_8_3(self):
        """
        运维-设备管理
        """
        s = Steps().open(f"{BaseUrl}/shop/machine")
        # 机器唯一码搜索
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div.search_option_left.s-gap-6-15 > div:nth-child(1) > div > div > div > div > input').click()
        s.sleep(1)
        s.find('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(2)').click()
        s.sleep(1)
        # 输入机器唯一码 绑盘机2AD2253003021980
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div.search_option_left.s-gap-6-15 > div:nth-child(1) > div > input')
        s.type('2AD2253003021980')
        s.sleep(1)
        # 清空输入
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div.search_option_left.s-gap-6-15 > div:nth-child(1) > div > input')
        s.move_to_element()
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div.search_option_left.s-gap-6-15 > div:nth-child(1) > div > span').click()
        s.sleep(1)
        # 机器状态
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div.search_option_left.s-gap-6-15 > div:nth-child(4) > div > div.el-input.el-input--suffix > input').click()
        s.sleep(1)
        # 即将到期
        s.find('body > div:nth-child(6) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(3)').click()
        s.sleep(1)
        # 正常
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div.search_option_left.s-gap-6-15 > div:nth-child(4) > div > div.el-input.el-input--suffix > input').click()
        s.sleep(1)
        s.find('body > div:nth-child(6) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(2)').click()
        s.sleep(1)
        # 绑盘机
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div.search_option_left.s-gap-6-15 > div:nth-child(5) > div > div > input').click()
        s.sleep(1)
        s.find('body > div:nth-child(7) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(3)').click()
        s.sleep(1)

    def test_Afpn_8_3_1(self):
        """
        运维-设备管理-新增机器
        """
        s = Steps().open(f"{BaseUrl}/shop/machine")
        # 点击新增机器
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div.search_option_right.s-gap-6-10.s-g-l-0 > button').click()
        # 商户选择
        s.find('#app > section > section > section > main > section > section > main > div.main > div:nth-child(4) > div > div.el-dialog__body > div > div > form > div:nth-child(1) > div > div > div > input').click()
        s.sleep(1)
        s.find('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:last-child').click()
        s.sleep(1)
        # 选择档口
        s.find('#app > section > section > section > main > section > section > main > div.main > div:nth-child(4) > div > div.el-dialog__body > div > div > form > div:nth-child(2) > div > div > div > input').click()
        s.sleep(1)
        s.find('body > div:nth-child(7) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:last-child').click()
        s.sleep(1)
        # 输入机器名称
        s.find('#app > section > section > section > main > section > section > main > div.main > div:nth-child(4) > div > div.el-dialog__body > div > div > form > div:nth-child(3) > div > div > input')
        s.type('测试')
        # 输入机器唯一码
        s.find('#app > section > section > section > main > section > section > main > div.main > div:nth-child(4) > div > div.el-dialog__body > div > div > form > div:nth-child(4) > div > div > input')
        s.type('AP-W3000AF20230901061')
        # 选择设备类型 称重机
        s.find('#app > section > section > section > main > section > section > main > div.main > div:nth-child(4) > div > div.el-dialog__body > div > div > form > div:nth-child(5) > div > div > div > input').click()
        s.sleep(1)
        s.find('body > div:nth-child(8) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1)').click()
        s.sleep(1)
        # 选择设备型号
        s.find('#app > section > section > section > main > section > section > main > div.main > div:nth-child(4) > div > div.el-dialog__body > div > div > form > div:nth-child(6) > div > div.el-select.common_width_de > div > input').click()
        s.sleep(1)
        s.find('body > div:nth-child(9) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(6)').click()  
        s.sleep(1)
        # 到期时间永久
        s.find('#app > section > section > section > main > section > section > main > div.main > div:nth-child(4) > div > div.el-dialog__body > div > div > form > div:nth-child(7) > div > div > label:nth-child(1) > span.el-radio__input > span').click()
        # 点击确定
        s.find('#app > section > section > section > main > section > section > main > div.main > div:nth-child(4) > div > div.el-dialog__footer > div > button.el-button.common_button.el-button--primary').click()
        s.sleep(1)
        # 提示:机器唯一码已存在
        self.assertText('机器唯一码已存在')
        self.assertStatusCode(status_code=200)

    def test_Afpn_8_4(self):
        """
        运维-打印机管理
        """
        s = Steps().open(f"{BaseUrl}/shop/printer")
        # 商户名称
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div.search_option_left.s-gap-6-15 > div:nth-child(2) > div > div > input').click()
        s.sleep(1)
        s.find('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:last-child').click()
        s.sleep(1)
        # 档口名称
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div.search_option_left.s-gap-6-15 > div:nth-child(3) > div > div > input').click()
        s.sleep(1)
        s.find('body > div:nth-child(6) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:last-child').click()
        s.sleep(1)

    def test_Afpn_8_5(self):
        """
        运维-人脸激活码管理
        """
        s = Steps().open(f"{BaseUrl}/shop/activation")
        # 激活状态 未激活
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div.s-h-top.s-justify-between > div.search_option_left.s-gap-6-15 > div:nth-child(3) > div > div > input').click()
        s.sleep(1)
        s.find('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1)').click()
        s.sleep(1)

    def test_Afpn_8_6(self):
        """
        运维-公众号模板管理
        """
        s = Steps().open(f"{BaseUrl}/shop/wechatIndustryTemplate")
        # 激活状态 未激活
        pass

    def test_Afpn_8_7(self):
        """
        运维-应用管理
        """
        s = Steps().open(f"{BaseUrl}/shop/application")
        # 应用类型 微信小程序
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div.search_option_left.s-gap-6-15 > div:nth-child(2) > div > div > input').click()
        s.sleep(1)
        s.find('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(2)').click()
        s.sleep(1)

    def test_Afpn_8_8(self):
        """
        运维-小程序跳转
        """
        s = Steps().open(f"{BaseUrl}/shop/mpJump")
        # 输入小程序名称
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div.search_option_left.s-gap-6-15 > div:nth-child(2) > div > input')
        s.type('生活亿象')
        s.sleep(1)

    def test_Afpn_8_9(self):
        """
        运维-阿里短信管理
        """
        s = Steps().open(f"{BaseUrl}/shop/aliyunSmsConfig")
        # 输入小程序名称
        pass

    def test_Afpn_8_10(self):
        """
        运维-短信模板管理
        """
        s = Steps().open(f"{BaseUrl}/shop/smsTemplateManage")
        # 商户名称
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div > div:nth-child(1) > div > div > input').click()
        s.sleep(1)
        s.find('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(126)').click()
        s.sleep(1)

    def test_Afpn_9(self):
        """
        采购-计量单位
        """
        s = Steps().open(f"{BaseUrl}/purchase/measureUnit")
        # 计量类型
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div.search_option_left.s-gap-6-15 > div:nth-child(2) > div > div.el-input.el-input--suffix > input').click()
        s.sleep(1)
        s.find('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1)').click()
        s.sleep(1)

    def test_Afpn_10_1(self):
        """
        安全-经营角色管理
        """
        s = Steps().open(f"{BaseUrl}/safe/masterRole")
        s.sleep(1)


    def test_Afpn_10_2(self):
        """
        安全-总部角色
        """
        s = Steps().open(f"{BaseUrl}/safe/role/head")
        # 角色状态 启用
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div.search_option_left.s-gap-6-15 > div:nth-child(2) > div > div.el-input.el-input--suffix > input').click()
        s.sleep(1)
        s.find('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1)').click()
        s.sleep(1)

    def test_Afpn_10_3(self):
        """
        安全-商户角色
        """
        s = Steps().open(f"{BaseUrl}/safe/role/merchant")
        # 角色状态 启用
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div.search_option_left.s-gap-6-15 > div:nth-child(2) > div > div > input').click()
        s.sleep(1)
        s.find('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1)').click()
        s.sleep(1)

    def test_Afpn_10_4(self):
        """
        安全-档口角色
        """
        s = Steps().open(f"{BaseUrl}/safe/role/store")
        # 角色状态 启用
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div.search_option_left.s-gap-6-15 > div:nth-child(2) > div > div > input').click()
        s.sleep(1)
        s.find('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1)').click()
        s.sleep(1)


    def test_Afpn_10_5(self):
        """
        安全-业主角色
        """
        s = Steps().open(f"{BaseUrl}/safe/role/owner")
        # 角色状态 启用
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div.search_option_left.s-gap-6-15 > div:nth-child(2) > div > div > input').click()
        s.sleep(1)
        s.find('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1)').click()
        s.sleep(1)

    def test_Afpn_10_6(self):
        """
        安全-合作商角色
        """
        s = Steps().open(f"{BaseUrl}/safe/role/coop")
        # 角色状态 启用
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div.search_option_left.s-gap-6-15 > div:nth-child(2) > div > div.el-input.el-input--suffix > input').click()
        s.sleep(1)
        s.find('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1)').click()
        s.sleep(1)

    def test_Afpn_10_7(self):
        """
        安全-账号管理
        """
        s = Steps().open(f"{BaseUrl}/safe/masterUser")
        # 选择手机号搜索
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div.search_option_left.s-gap-6-15 > div:nth-child(1) > div > div > div > div.el-input.el-input--suffix > input').click()
        s.sleep(1)
        s.find('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(2)').click()
        s.sleep(1)
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div.search_option_left.s-gap-6-15 > div:nth-child(1) > div > input')
        s.type('15900506255')
        s.sleep(1)

    def test_Afpn_10_8(self):
        """
        安全-权限列表
        """
        s = Steps().open(f"{BaseUrl}/safe/permission/manageWeb")
        s.sleep(1)
        # 商户名称

    def test_Afpn_10_9(self):
        """
        安全-权限分配
        """
        s = Steps().open(f"{BaseUrl}/safe/permission/assign")
        s.sleep(1)
        # 商户名称

    def test_Afpn_10_10(self):
        """
        安全-登录日志
        """
        s = Steps().open(f"{BaseUrl}/safe/sys/loginLog")
        s.sleep(1)
        # 商户名称

    def test_Afpn_10_11(self):
        """
        安全-操作日志
        """
        s = Steps().open(f"{BaseUrl}/safe/sys/operateLog")
        s.sleep(1)
        # 商户名称
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div > div:nth-child(1) > div > div.el-input.el-input--suffix > input').click()
        s.sleep(1)
        s.find('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1)').click()
        s.sleep(1)

    def test_Afpn_10_12(self):
        """
        安全-告警通知
        """
        s = Steps().open(f"{BaseUrl}/safe/sys/alarm")
        s.sleep(1)
        # 清空日期
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div > div:nth-child(4) > div')
        s.move_to_element()
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div > div:nth-child(4) > div > i.el-input__icon.el-range__close-icon').click()
        s.sleep(1)


    def test_Afpn_10_13(self):
        """
        安全-版本管理
        """
        s = Steps().open(f"{BaseUrl}/safe/version/manage")
        s.sleep(1)
        # 商户名称


    def test_Afpn_11(self):
        """
        三方-API访问限制
        """
        s = Steps().open(f"{BaseUrl}/external/openApi")
        s.sleep(1)
        # 商户名称
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div.search_option_left.s-gap-6-15 > div:nth-child(1) > div > input')
        s.type('艾佩')
        s.sleep(1)
        # 清空名称
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div.search_option_left.s-gap-6-15 > div:nth-child(1) > div > input')
        s.move_to_element()
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div.search_option_left.s-gap-6-15 > div:nth-child(1) > div > span').click()
        s.sleep(1)

    def test_Afpn_12_1(self):
        """
        菜品-规格管理
        """
        s = Steps().open(f"{BaseUrl}/dishFlavor/spec")
        # 商户名称
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div > div:nth-child(2) > div > div.el-input.el-input--suffix > input').click()
        s.sleep(1)
        s.find('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(126)').click()
        s.sleep(1)

    def test_Afpn_12_2(self):
        """
        菜品-口味管理
        """
        s = Steps().open(f"{BaseUrl}/dishFlavor/flavor")
        # 商户名称
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div > div:nth-child(2) > div > div.el-input.el-input--suffix > input').click()
        s.sleep(1)
        s.find('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(126)').click()
        s.sleep(1)

    def test_Afpn_12_3(self):
        """
        菜品-菜品分类
        """
        s = Steps().open(f"{BaseUrl}/dishFlavor/goodsCategory")
        # 商户名称
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div > div:nth-child(2) > div > div.el-input.el-input--suffix > input').click()
        s.sleep(1)
        s.find('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(126)').click()
        s.sleep(1)
        # 分类类型
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div > div:nth-child(4) > div > div > input').click()
        s.sleep(1)
        s.find('body > div:nth-child(6) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(2)').click()      
        s.sleep(1)

    def test_Afpn_12_4(self):
        """
        菜品-单品菜品
        """
        s = Steps().open(f"{BaseUrl}/dishFlavor/singleDish")
        # 商户名称
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div > div:nth-child(2) > div > div > input').click()
        s.sleep(1)
        s.find('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:last-child').click()
        s.sleep(1)
        # 档口名称
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div > div:nth-child(3) > div > div > input').click()
        s.sleep(1)
        s.find('body > div:nth-child(6) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:last-child').click()
        s.sleep(1)
        # 计价方式
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div > div:nth-child(5) > div > div > input').click()
        s.sleep(1)
        s.find('body > div:nth-child(7) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1)').click()
        s.sleep(1)
        # 菜品状态
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div > div:nth-child(6) > div > div > input').click()
        s.sleep(1)
        s.find('body > div:nth-child(8) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(2)').click()
        s.sleep(1)

    def test_Afpn_12_5(self):
        """
        菜品-单品组合
        """
        s = Steps().open(f"{BaseUrl}/dishFlavor/dishGroup")
        # 商户名称
        s.sleep(1)

    def test_Afpn_12_6(self):
        """
        菜品-套餐菜品
        """
        s = Steps().open(f"{BaseUrl}/dishFlavor/packageDish")
        # 商户名称
        s.sleep(1)

    def test_Afpn_12_7(self):
        """
        菜品-菜谱分组
        """
        s = Steps().open(f"{BaseUrl}/dishFlavor/kitchenGroup")
        # 商户名称
        s.sleep(1)

    def test_Afpn_12_8(self):
        """
        菜品-菜谱分类
        """
        s = Steps().open(f"{BaseUrl}/dishFlavor/kitchenGoodsCategory")
        # 商户名称
        s.sleep(1)

    def test_Afpn_12_9(self):
        """
        菜品-原料管理
        """
        s = Steps().open(f"{BaseUrl}/dishFlavor/kitchenMaterial")
        # 商户名称
        s.sleep(1)

    def test_Afpn_12_10(self):
        """
        菜品-调料管理
        """
        s = Steps().open(f"{BaseUrl}/dishFlavor/kitchenFlavour")
        # 类型
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div.search_option_left.s-gap-6-15 > div:nth-child(2) > div > div > input').click()
        s.sleep(1)
        s.find('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(3)').click()
        s.sleep(1)

    def test_Afpn_12_11(self):
        """
        菜品-平台菜谱
        """
        s = Steps().open(f"{BaseUrl}/dishFlavor/kitchen/platformMenu")
        # 版本状态
        s.find('#app > section > section > section > main > section > section > main > div.main > div.s-card > div > div.search_option_left.s-gap-6-15 > div:nth-child(5) > div > div.el-input.el-input--suffix > input').click()
        s.sleep(1)
        s.find('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1)').click()
        s.sleep(1)
        # 切换到蒸烤箱
        s.find('#tab-2').click()
        s.sleep(1)



    def test_Afpn_12_12(self):
        """
        菜品-菜谱授权
        """
        s = Steps().open(f"{BaseUrl}/dishFlavor/kitchenMenuLicense")
        # 商户名称
        s.sleep(1)



if __name__ == '__main__':
    seldom.main(
                case='test_apfn_1.AfpnTest',
                browser="gc", 
                # browser="firefox",
                tester="tzk",
                description="数字餐厅管理端",
                # debug=True
                )



    