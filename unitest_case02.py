#coding = utf-8
import unittest
import os
import HTMLTestRunner
class Fristcase02(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("所有case的前置条件")
    @classmethod
    def tearDownClass(cls):
        print("所有case的后置条件")
    def setUp(self):
        print("这是前置条件")
    def tearDown(self):
        print("这是后置条件")
    @unittest.skip("跳过第零一条case")
    def testcase001(self):
        print("这是第零一条case")
    def testcase002(self):
        print("这是第零二条case")
    def testcase003(self):
        print("这是第零三条case")

if __name__ == '__main__':
    # unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTest(Fristcase02('testcase002'))
    # suite.addTest(Fristcase02('testcase003'))
    # suite.addTest(Fristcase02('testcase001'))
    # unittest.TextTestRunner().run(suite)
    file_path = os.path.join(os.getcwd()+"/report/"+"fristcase.html")  # 获取测试报告地址
    f = open(file_path,'wb')
    # 执行某一条case#
    suite = unittest.TestSuite()
    suite.addTest(Fristcase02('testcase003'))
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='UI自动化报告', description='UI自动化详细报告', verbosity=2)
    runner.run(suite)