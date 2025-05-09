import seldom, requests, os
from seldom import Steps

import base64
from PIL import Image
from io import BytesIO

import pytesseract, cv2
import numpy as np


def save_base64_image(base64_str, save_path):
    # 解码Base64字符串
    image_data = base64.b64decode(base64_str)
    
    # 使用PIL创建图像对象
    image = Image.open(BytesIO(image_data))
    
    # 保存图像到指定路径
    image.save(save_path)
    print(f"Image saved as {save_path}")

def save_to_txt(text, file_path):
    with open(file_path, 'w') as file:
        file.write(text)

def recognize_captcha(image_path):
    # 打开图片
    image = Image.open(image_path)

    # 将图像转换为灰度图像
    image = image.convert('L')

    # 对图像进行二值化处理
    threshold = 127
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    image = image.point(table, '1')

    


    
    # 使用pytesseract识别图片中的文本
    text = pytesseract.image_to_string(image, lang='eng', config='--psm 7 --oem 3 -c tessedit_char_whitelist=0123456789')
    
    # 过滤非数字字符，只保留数字
    digits = ''.join(filter(str.isdigit, text))
    
    return digits


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
        
        
        s.find('#app > div > div.login-box.s-h-center > form > div:nth-child(2) > div > div > input').type("18335161013")
        s.find('#app > div > div.login-box.s-h-center > form > div:nth-child(3) > div > div > input').type("112233")
        # 获取验证码图片的URL
        captcha_url = self.get_attribute(css="#app > div > div.login-box.s-h-center > form > div:nth-child(4) > div > div > div.login-kaptcha-code > img", attribute="src")
        # print(captcha_url)

        # 获取图片的base64编码信息
        base64_str = captcha_url.split(",")[1]
        # print(base64_str)
        save_to_txt(base64_str, file_path="pic/captcha_base64.txt")


        # 下载验证码图片并保存到本地
        captcha_image = save_base64_image(base64_str, save_path="pic/captcha.png")

        # 识别验证码图片中的文本
        # captcha_text = recognize_captcha('pic/captcha.png')
        # print(f"Captcha text: {captcha_text}")

        image = cv2.imread('pic/20250401.png')

        # 转换为HSV颜色空间
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # 定义蓝色的HSV范围
        lower_blue = np.array([100, 50, 50])
        upper_blue = np.array([130, 255, 255])

        # 创建掩码
        mask = cv2.inRange(hsv, lower_blue, upper_blue)

        # 应用掩码
        result = cv2.bitwise_and(image, image, mask=mask)
        cv2.imwrite("pic/captcha_result.png", result)

        # 转换为灰度图像
        gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
        cv2.imwrite("pic/captcha_gray.png", gray)

        # 二值化处理
        _, binary1 = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
        cv2.imwrite("pic/captcha_binary100.png", binary1)
        _, binary2 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
        cv2.imwrite("pic/captcha_binary127.png", binary2)
        _, binary3 = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
        cv2.imwrite("pic/captcha_binary150.png", binary3)

        # 去除干扰线（如果有）
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
        eroded = cv2.erode(binary1, kernel, iterations=1)
        cleaned = cv2.dilate(eroded, kernel, iterations=1)
        cv2.imwrite("pic/cleaned_captcha_cleaned.png", cleaned)

        # 使用Tesseract进行识别，指定只识别数字
        custom_config = r'--oem 3 --psm 7 -c tessedit_char_whitelist=0123456789'
        captcha_text = pytesseract.image_to_string(image, lang='eng', config=custom_config)

        print(f"Captcha text: {captcha_text}")

        # 输入验证码文本
        s.find('#app > div > form > div:nth-child(4) > div > div > div.login-input-code.el-input.el-input--prefix > input').type(captcha_text)
        s.sleep(1)
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
