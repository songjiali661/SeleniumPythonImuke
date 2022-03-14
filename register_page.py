#coding = utf-8
from base.find_element import FindElement
class RegisterPage(object):
    def __init__(self,driver):
        self.fd = FindElement(driver)
    #获取邮箱
    def get_email_element(self):
        return self.fd.get_element('email')
    #获取用户名
    def get_name_element(self):
        return self.fd.get_element('name')
    #获取密码
    def get_password_element(self):
        return self.fd.get_element('password')
    #获取验证码
    def get_code_element(self):
        return self.fd.get_element('code')
    #点击事件
    def get_btn_element(self):
        return self.fd.get_element('register_button')
    #获取错误邮箱提示
    def get_email_error(self):
        return self.fd.get_element('email_error')

    #获取错误用户名提示
    def get_name_error(self):
        return self.fd.get_element('name_error')
    #获取错误密码提示
    def get_password_error(self):
        return self.fd.get_element('password')
    #获取错误的验证码提示
    def get_code_error(self):
        return self.fd.get_element('code')
