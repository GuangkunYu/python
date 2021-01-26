import sqlite3
import json
import xlrd


def run_database(datafile,sql_list):
    conn = sqlite3.connect(datafile)
    for sql in sql_list:
        print(sql)
        conn.execute(sql)
        conn.commit()


INSERT_SQL_VALUE = "INSERT INTO mqtt点表(位置,点类型,参数序号,位号,阈值,倍数,值,描述,设备号,状态,模块号) VALUES('{}',{},{},{},{},{},0,None,{},{},{})"


def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        data = json.loads(content)
        return data


def insert_sql(station, data, 设备号):
    sql = []
    for s in zip(station, 设备号):
        for key, value in data['点类型'].items():
            insert_sql = INSERT_SQL_VALUE.format(
                str(s[0]), key, data['参数序号'], value, data['阈值'], data['倍数'], s[1], data['状态'], s[1]).replace('None', 'null')
            sql.append(insert_sql)
    return sql


def read_excel(excel_file, facturer, drive_name):
    data = xlrd.open_workbook(excel_file)
    table = data.sheet_by_name(facturer)
    drive_names = table.row_values(0, start_colx=0, end_colx=None)
    #print(drive_names)
    for name in drive_names:
        if name == drive_name:
            index = drive_names.index(name)
            break
    position = table.col_values(index, start_rowx=2, end_rowx=None)
    position2 = [i for i in position if i != '']
    drive_num = table.col_values(index + 1, start_rowx=2, end_rowx=None)
    drive_num2 = [i for i in drive_num if i != '']
    return position2, drive_num2


def main():
    # 数据库文件路径
    data_file = 'D:\\OneDrive - ncist.edu.cn\\work\\智能运维子站部署资料\\00-0.0.6 - copy.db'
    # json文件路径
    file_name = 'data3.json'
    # 厂商名称
    facturer = '微辰主机'
    # 设备名称
    drive_name = '四合一传感器'
    excel_file = '设备清单.xlsx'
    pos, nums = read_excel(excel_file, facturer, drive_name)
    data = read_file(file_name)
    sql = insert_sql(pos, data[facturer][drive_name], nums)
    for s in sql:
        print(s)
    run_database(data_file, sql)

def test():
    # 数据库文件路径
    data_file = 'D:\\OneDrive - ncist.edu.cn\\work\\智能运维子站部署资料\\00-0.0.6 - copy.db'
    sql = "INSERT INTO mqtt点表(位置,点类型,参数序号,位号,阈值,倍数,值,描述,设备号,状态,模块号) VALUES(4#变压器室四合一气体2,16527,20,1,null,null,0,null,232.0,0,232.0)"
    sql2 = "select * from mqtt点表"
    run_database(data_file, sql)


if __name__ == "__main__":
    main()

