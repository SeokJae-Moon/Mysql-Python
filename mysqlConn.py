
import pymysql

conn = pymysql.connect(host='localhost', user='root', password='1234', db='testdb', charset='utf8')

curs = conn.cursor()

sql = "select * from member"
curs.execute(sql)

rows = curs.fetchall()
print(rows)

conn.close()

#------------------------------------------------------------------------------------#

conn = pymysql.connect(host='localhost', user='root', password='1234', db='testdb', charset='utf8')

curs = conn.cursor()
sql = """insert into member(email)
         values (%s)"""
curs.execute(sql, ('Hang@'))
curs.execute(sql, ('Seok'))

data = (('Ahan'),
        ('Bom'))
sql = """insert into member(memID) values (%s)"""
curs.executemany(sql, data)
conn.commit()

conn.close()

# #-----------------------------------------------------------------------------------------
conn = pymysql.connect(host='localhost', user='root', password='1234', db='testdb', charset='utf8')

curs = conn.cursor()
sql = """update member
         set idx = 1
         where memID = 'MSJ'"""
curs.execute(sql)

#sql = "delete from customer where id=%s"
#curs.execute(sql, 6)

conn.commit()
conn.close()

#-----------------------------------------------------------------

conn = pymysql.connect(host='localhost', user='root', password='1234',
                       db='testdb', charset='utf8')

try:
    # INSERT
    with conn.cursor() as curs:
        #sql = "insert into member(name,category,region) values (%s, %s, %s)"
        #curs.execute(sql, ('이광수', 1, '서울'))
        sql = "insert into member(memID) values (%s)"
        curs.execute(sql, ('kwang'))

    conn.commit()

    # SELECT
    with conn.cursor() as curs:
        sql = "select * FROM member"
        curs.execute(sql)
        rs = curs.fetchall()
        for row in rs:
            print(row)

finally:
    conn.close()