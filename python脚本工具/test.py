# import sqlite3
# class UseData(object):
#     """
#     docstring
#     """
#     def __init__(self):
#         self.coon = sqlite3.connect(r'E:\LDDQ\子站工作\test\00-0.0.1.db')

#     def get_parameter_serial_number(self):
#         cursor = self.coon.cursor()
#         sql = 'select 参数序号 from 服务参数 where 描述="微辰主机"'
#         res = cursor.execute(sql)
#         print(res.fetchone())

#     def get_point_type(self):




# if __name__ == "__main__":
#     ud = UseData()
#     ud.get_parameter_serial_number()

# d = {'a': 1, 'b':2}
# for i in d:
#     print(i)
#     print(d.value())