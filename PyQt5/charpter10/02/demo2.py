import pymysql

db = pymysql.connect('192.168.4.192', 'root', 'root', 'ygk-qt5')

cursor = db.cursor()

sql1 = 'drop table if exists books;'
cursor.execute(sql1)

sql2 = """
    create table books(
    id int(8) not null auto_increment,
    name varchar(50) NOT NULL ,
    category varchar(50) NOT NULL ,
    price decimal(10, 2) DEFAULT NULL ,
    publish_time date DEFAULT NULL ,
    PRIMARY KEY (id)
)engine=MyISAM auto_increment=1 default charset=utf8;
"""
cursor.execute(sql2)

db.close()
