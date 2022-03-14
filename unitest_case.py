#coding = utf-8
import unittest
class Fristcase01(unittest.TestCase):
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
    @unittest.skip("跳过第一条case")
    def testcase01(self):
        print("这是第一条case")
    def testcase02(self):
        print("这是第二条case")
    def testcase03(self):
        print("这是第三条case")

if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(Fristcase01('testcase02'))
    suite.addTest(Fristcase01('testcase03'))
    suite.addTest(Fristcase01('testcase01'))
    unittest.TextTestRunner().run(suite)
