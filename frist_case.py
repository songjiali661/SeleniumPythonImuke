#coding = utf-8
import sys
sys.path.append(r'E:\\imuke')
from business.register_business import RegisterBusiness
from selenium import webdriver
import time
import unittest
import warnings
import os
import HTMLTestRunner #生成报告
from log.register_log import RegisterLog
class FristCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.log = RegisterLog()
        cls.logger = cls.log.get_log()
    @classmethod
    def tearDownClass(cls):
        cls.log.close_handle()
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.binary_location = r'C:\Users\10787\AppData\Local\Google\Chrome\Application/chrome.exe'
        self.driver = webdriver.Chrome(options=options)
        self.driver.get('http://www.5itest.cn/register')
        self.driver.maximize_window()
        time.sleep(5)
        self.logger.info("this is chrom")

        self.register = RegisterBusiness(self.driver)
        warnings.simplefilter('ignore',ResourceWarning)
    def tearDown(self):
        #封装截图
        for method_name,error in self._outcome.errors:
            if error:
                case_name = self._testMethodName #获取用例名称
                file_path = os.path.join(os.getcwd()+'/report/'+case_name+'.png')
                self.driver.save_screenshot(file_path)
        self.driver.close()


    def test_register_email_error(self):
        email_error = self.register.register_email_erro('1','111111','1234466','test1')
        self.assertFalse(email_error)
        # if email_error == True:
        #     print('注册成功，此条case执行失败')
    def test_register_name_error(self):
        name_error = self.register.register_name_error('1078726974@qq.com', '11111', '1234466', 'test12')
        self.assertFalse(name_error)
        # if name_error == True:
        #     print('注册成功，此条case执行失败')
    def test_register_password_error(self):
        password_error = self.register.register_password_error('1078726974@qq.com', '111', '466', 'test12')
        self.assertFalse(password_error)
        # if password_error == True:
        #     print('注册成功，此条case执行失败')
    def test_register_code_error(self):
        password_error = self.register.register_code_error('1078726974@qq.com', '111', '466', '111111')
        self.assertFalse(password_error)
        # if password_error == True:
        #     print('注册成功，此条case执行失败')
    def test_register_success(self):
        success = self.register.user_base('1078726974@qq.com', '111111', '123456', '111111')
        self.assertFalse(success)
        # if self.register.register_success() == True:
        #     print("注册成功")
# def main():
#     frist = FristCase()
#     frist.test_register_email_error()
#     frist.test_register_name_error()
#     frist.test_register_password_error()
#     frist.test_register_code_error()
#     frist.test_register_success()
if __name__ == '__main__':
    # unittest.main()#执行全部case
    #生成测试报告
    file_path = os.path.join(os.getcwd()+"/report/"+"fristcase.html")#获取测试报告地址
    f = open(file_path,'wb')
    #执行某一条case#
    suite = unittest.TestSuite()
    suite.addTest(FristCase('test_register_email_error'))
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='UI自动化报告', description='UI自动化详细报告', verbosity=2)
    runner.run(suite)
    # f.close()
    # unittest.TextTestRunner().run(suite)



