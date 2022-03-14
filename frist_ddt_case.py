#coding = utf-8
#邮箱、用户名、密码、验证码、错误信息定位元素、错误提示信息
import ddt
import unittest
import sys
sys.path.append('E:\\imuke')
from selenium import webdriver
import HTMLTestRunner
import os
import time
from business.register_business import RegisterBusiness
import warnings
from read_ini.excel_util import ExcelUtil
#获取excel数据
ex = ExcelUtil()
data = ex.get_data()
@ddt.ddt
class FristDdCase(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.binary_location = r'C:\Users\10787\AppData\Local\Google\Chrome\Application/chrome.exe'
        self.driver = webdriver.Chrome(options=options)
        self.driver.get('http://www.5itest.cn/register')
        self.driver.maximize_window()
        time.sleep(5)
        self.register = RegisterBusiness(self.driver)
        warnings.simplefilter('ignore',ResourceWarning)
    def tearDown(self):
        #生成错误截图
        for method_name,error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = os.path.join(os.getcwd()+'/report/'+case_name+'.png')
                self.driver.save_screenshot(file_path)
        self.driver.close()
    # @ddt.data(
    #         ['12','宋佳莉','123456','code','email_error','请输入有效的电子邮件地址'],
    #         ['1078726974@qq.com', '宋佳莉', '123456', 'code', 'email_error', '请输入有效的电子邮件地址'],
    #     )
    # @ddt.unpack
    @ddt.data(*data)
    # @ddt.unpack
    def test_register_case(self,data):
        email,name,password,code,assertCode,assertText = data
        email_error = self.register.register_function(email,name,password,code,assertCode,assertText)
        self.assertFalse(email_error,'测试失败')
        # print(data)



if __name__ == '__main__':
    #unittest.main()
    file_path = os.path.join(os.getcwd()+"/report/"+"fristcase.html")  # 获取测试报告地址
    f = open(file_path,'wb')
    # 执行某一条case#
    suite = unittest.TestLoader().loadTestsFromTestCase(FristDdCase)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='UI自动化报告1', description='UI自动化详细报告1', verbosity=2)
    runner.run(suite)
