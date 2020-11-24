import pymysql

# 打开数据库连接，参数1：数据库域名或IP，参数2：数据库账号；参数3：数据库密码；参数4：数据库名称
db = pymysql.connect("192.168.4.192", "root", "root", "ygk-qt5", charset="utf8")

# 使用cursor()方法创建一个游标对象cursor
cursor = db.cursor()

# 数据列表
data = [
    ("零基础学Python", 'Python', '79.80', '2018-5-20'),
    ("Python从入门到实践", 'Python', '99.80', '2019-6-18'),
    ("PyQt5从入门到实践", 'Python', '69.80', '2020-5-21'),
    ("OpenCV从入门到实践", 'Python', '69.80', '2020-5-21'),
    ("Python算法从入门到实践", 'Python', '69.80', '2020-5-21'),
]

try:
    # 使用executemany()方法执行SQL, 插入多条数据
    cursor.executemany("insert into books(name, category, price, publish_time) values (%s, %s, %s, %s)", data)
    # 提交数据
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()

# 关闭数据库连接
db.close()
