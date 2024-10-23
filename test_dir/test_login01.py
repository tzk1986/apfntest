import seldom, requests, os
from seldom import Steps

import base64
from PIL import Image
from io import BytesIO

import pytesseract, cv2



def save_base64_image(base64_str, save_path):
    # 解码Base64字符串
    image_data = base64.b64decode(base64_str)
    
    # 使用PIL创建图像对象
    image = Image.open(BytesIO(image_data))
    
    # 保存图像到指定路径
    image.save(save_path)
    print(f"Image saved as {save_path}")



# def recognize_captcha(image_path):
#     # 打开图片
#     image = Image.open(image_path)

#     # 将图像转换为灰度图像
#     image = image.convert('L')

#     # 对图像进行二值化处理
#     threshold = 127
#     table = []
#     for i in range(256):
#         if i < threshold:
#             table.append(0)
#         else:
#             table.append(1)
#     image = image.point(table, '1')

    


    
#     # 使用pytesseract识别图片中的文本
#     text = pytesseract.image_to_string(image, lang='eng', config='--psm 7 --oem 3 -c tessedit_char_whitelist=0123456789')
    
#     # 过滤非数字字符，只保留数字
#     digits = ''.join(filter(str.isdigit, text))
    
#     return digits


def download_image(url, save_path):
    if os.path.exists(save_path):
        os.remove(save_path)  # 删除已存在的文件
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"Image downloaded and saved as {save_path}")
    else:
        print(f"Failed to download image. Status code: {response.status_code}")


# 测试环境 数字餐厅管理端
# BaseUrl = "http://10.50.11.120:9002"

# 预发布环境
BaseUrl = "https://toc.epfly.com.cn/"


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
        s = Steps().open(f"{BaseUrl}/login")
        
        
        s.find('#app > div > form > div:nth-child(2) > div > div > input').type("18335161013")
        s.find('#app > div > form > div:nth-child(3) > div > div > input').type("112233")
        # 获取验证码图片的URL
        captcha_url = self.get_attribute(css="#app > div > form > div:nth-child(4) > div > div > div.login-kaptcha-code > img", attribute="src")
        # print(captcha_url)

        # 获取图片的base64编码信息
        base64_str = captcha_url.split(",")[1]
        # print(base64_str)

        # 下载验证码图片并保存到本地
        captcha_image = save_base64_image(base64_str, save_path="test_dir/captcha.png")

        # 识别验证码图片中的文本
        # captcha_text = recognize_captcha('test_dir/captcha.png')
        # print(f"Captcha text: {captcha_text}")

        image = cv2.imread('test_dir/captcha.png')

        # 转换为灰度图像
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # 二值化处理
        _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

        # 去除干扰线（如果有）
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        eroded = cv2.erode(binary, kernel, iterations=1)
        cleaned = cv2.dilate(eroded, kernel, iterations=1)

        # 使用Tesseract进行识别，指定只识别数字
        custom_config = r'--oem 3 --psm 7 -c tessedit_char_whitelist=0123456789'
        captcha_text = pytesseract.image_to_string(cleaned, lang='eng', config=custom_config)

        print(f"Captcha text: {captcha_text}")
        # 测试一下
        print("测试一下")

        # 输入验证码文本
        s.find('#app > div > form > div:nth-child(4) > div > div > div.login-input-code.el-input.el-input--prefix > input').type(captcha_text)
        
        s.find('#app > div > form > div:nth-child(5) > div > button').click()


        s.sleep(1)
        self.get_cookies()
        print(self.get_cookies())
        






if __name__ == '__main__':
    seldom.main(
                case='test_login01',
                browser="gc", 
                # browser="firefox",
                tester="tzk",
                debug=True
                )
