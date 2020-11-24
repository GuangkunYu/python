import sqlite3

# 连接到sqlite数据库
# 数据库文件是mrsoft.db，如果文件不存在，会自动在当前目录创建
conn = sqlite3.connect('mrsoft.db')

# 创建游标对象
cursor = conn.cursor()

# 执行一条SQL语句，创建user表
# sql = 'create table user (id int(10) primary key, name varchar(20))'
# 插入数据
# sql1 = 'insert into user (id, name) values (1, "MRSOFT")'
# sql2 = 'insert into user (id, name) values (2, "Andy")'
# sql3 = 'insert into user (id, name) values (3, "明日科技小助手")'
# 查询数据
# sql = 'select * from user'
sql = 'select * from user where id>?'
# cursor.execute(sql1)
# cursor.execute(sql2)
# cursor.execute(sql3)
cursor.execute(sql, (1,))

# 获取查询结果
# result = cursor.fetchone()
# result = cursor.fetchall()
# result = cursor.fetchmany(2)
result = cursor.fetchall()
print(result)
# 关闭游标
cursor.close()

# 提交事务
conn.commit()

# 关闭数据库连接
conn.close()