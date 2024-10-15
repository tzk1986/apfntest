from poium import Page, Element


class BingPage(Page):
    """baidu page"""
    search_input = Element(id_="sb_form_q")
    search_button = Element(tag="svg")



class AfpnPage(Page):
    """经营管理登录 page"""
    name_input = Element('//*[@id="app"]/div/form/div[1]/div/div/input',description="用户名")
    password_input = Element('//*[@id="app"]/div/form/div[2]/div/div/input', description="密码")
    code_input = Element('//*[@id="app"]/div/form/div[3]/div/div/div[1]/input', description="验证码")
    login_button = Element('//*[@id="app"]/div/form/div[4]/div/button', description="登录")
    # name_input = Element(xpath="/html/body/div[1]/div/form/div[1]/div/div/input",index=0, description="用户名")
    # password_input = Element(xpath="/html/body/div[1]/div/form/div[2]/div/div/input", description="密码")
    # code_input = Element(xpath="/html/body/div[1]/div/form/div[3]/div/div/div[1]/input", description="验证码")
    # login_button = Element(xpath="/html/body/div[1]/div/form/div[4]/div/button", description="登录")


    # name_input = Element(selector="#app > div > form > div:nth-child(2) > div > div > input", description="用户名")
    # password_input = Element(selector="#app > div > form > div:nth-child(3) > div > div > input", description="密码")
    # code_input = Element(selector="#app > div > form > div:nth-child(4) > div > div > div.login-input-code.el-input.el-input--prefix > input", description="验证码")
    # login_button = Element(selector="#app > div > form > div:nth-child(5) > div > button", description="登录")
    # test_input = Element(xpath="//*[@id=")

class AfpnPage_2_1(Page):
    """经营管理-入驻-总部 page"""
  

    """企业简称搜索"""

    search_input_1 = Element('//*[@id="app"]/section/section/section/main/section/section/main/div[1]/div[2]/div/div[1]/div[1]/div/input',
                             description="企业简称搜索")

    """状态搜索"""
    search_input_2 = Element('//*[@id="app"]/section/section/section/main/section/section/main/div[1]/div[2]/div/div[1]/div[2]/div/div[1]/input',
                            description="状态搜索")

    """查询"""
    search_button = Element('//*[@id="app"]/section/section/section/main/section/section/main/div[1]/div[2]/div/div[1]/div[3]/button',
                            description="查询")
    pass

class AfpnPage_2_2(Page):
    """经营管理-入驻-业主 page"""

    pass

class AfpnPage_3_1(Page):
    """经营管理-商户-商户列表 page"""

    pass

class AfpnPage_3_2(Page):
    """经营管理-商户-档口列表 page"""
    pass

class AfpnPage_4_1(Page):
    """经营管理-会员-平台会员 page"""
    pass

class AfpnPage_4_2(Page):
    """经营管理-会员-商户会员 page"""
    pass

class AfpnPage_4_3(Page):
    """经营管理-会员-员工列表 page"""
    pass

