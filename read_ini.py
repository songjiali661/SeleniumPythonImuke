#coding = utf-8
import configparser
class ReadIin(object):
    def __init__(self,filename=None,node=None):
        if filename == None:
            filename = 'E:/imuke/config/config.ini'
        if node == None:
            self.node = 'RegisterElement'
        else:
            self.node = node
        self.cf = self.get_filename(filename)
    #获取文件
    def get_filename(self,filename):
        cf = configparser.ConfigParser()
        #读取文件地址
        cf.read(filename)
        return cf
    #获取vaule值
    def get_vaule(self,key):
        data = self.cf.get(self.node,key)
        return data


if __name__ == '__main__':
    read = ReadIin()
    print(read.get_vaule('email'))
