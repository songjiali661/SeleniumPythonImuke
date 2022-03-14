#coding = utf-8
import unittest
import os
class RunCase(unittest.TestCase):
    def test_case01(self):
        case_path = os.path.dirname(__file__)#获取用例文件地址
        suite = unittest.defaultTestLoader.discover(case_path,'unitest_*.py')#相当于一个容器
        unittest.TextTestRunner().run(suite)

if __name__ == '__main__':
    unittest.main()