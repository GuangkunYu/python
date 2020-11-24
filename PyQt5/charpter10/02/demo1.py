import pymysql

# 打开数据库连接，参数1：数据库域名或IP，参数2：数据库账号；参数3：数据库密码；参数4：数据库名称
db = pymysql.connect("192.168.4.192", "root", "root", "ygk-qt5")

# 使用cursor()方法创建一个游标对象cursor
cursor = db.cursor()

# 使用execute()方法执行SQL查询
cursor.execute("select version()")

# 使用fetchone()方法获取单条数据
data = cursor.fetchone()
print(f"database version: {data}")

# 关闭数据库连接
db.close()