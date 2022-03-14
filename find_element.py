#coding = utf-8
from read_ini.read_ini import ReadIin
class FindElement(object):
    def __init__(self,driver):
        self.driver = driver
    def get_element(self,key):
        read_ini = ReadIin()
        data = read_ini.get_vaule(key)
        by = data.split('>')[0]
        value = data.split('>')[1]
        try:
            if by == 'id':
                return self.driver.find_element_by_id(value)
            elif by == "name":
                return self.driver.find_element_by_name(value)
            else:
                return self.driver.find_element_by_class(value)
        except:
            #运行失败截图
            #self.driver.save_screenshot('E:/imuke/image/%s.png' %value)
            return None

