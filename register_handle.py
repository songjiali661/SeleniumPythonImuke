#coding = utf-8
from page.register_page import RegisterPage
class RegisterHandle(object):
    def __init__(self,driver):
        self.register_p = RegisterPage(driver)
    #输入邮箱
    def send_email(self,email):
        self.register_p.get_email_element().send_keys(email)
    #输入用户名
    def send_name(self,name):
        self.register_p.get_name_element().send_keys(name)
    #输入密码
    def send_password(self,password):
        self.register_p.get_password_element().send_keys(password)
    #输入验证码
    def send_code(self,code):
        self.register_p.get_code_element().send_keys(code)
    #获取文字信息
    def get_text(self,infor,user_info):#user_info表示错误的文案
        try:
            if infor == 'email_error':
                text = self.register_p.get_email_error().text
            elif infor == 'name_error':
                text = self.register_p.get_name_error().text
            elif infor == 'password_error':
                text = self.register_p.get_password_error().text
            else:
                text = self.register_p.get_code_error().text
        except:
            return None
        return text
    #点击注册按钮
    def click_register_btn(self):
        self.register_p.get_btn_element().click()

    #获取注册按钮文字
    def get_register_text(self):
        return self.register_p.get_btn_element().text


