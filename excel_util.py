#coding = utf-8
import xlrd
from xlutils.copy import copy
class ExcelUtil(object):
    def __init__(self,excel_path=None,index=None):
        if excel_path == None:
            excel_path = 'E:\imuke\config\casedata.xls'
        if index == None:
            index = 0
        #获取表数据
        self.data = xlrd.open_workbook(excel_path)
        self.table = self.data.sheets()[index]
        #行数
        # self.rows = self.table.nrows
    #获取excel数据，按照每行一个list，添加到一个大的list里面
    def get_data(self):
        result=[]
        for i in range(self.get_lins()):
            col = self.table.row_values(i)
            result.append(col) #获取的值写入列表
        return result
    #获取行数
    def get_lins(self):
        rows = self.table.nrows
        return rows
    #获取单元格数据
    def get_col_value(self):
        data = self.table.cell(4,3).value
        return data
    #写入数据
    def write_value(self,row,cell):
        #读取表数据
        read_value = self.data
        #copy表数据
        write_data = copy(read_value)
        #获取第0个单元格数据
        write_data.get_sheet(0).write(row,7)

if __name__ == '__main__':
    ex=ExcelUtil('E:\imuke\config\data.xls')
    print(ex.get_col_value())