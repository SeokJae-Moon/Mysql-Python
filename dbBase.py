import os
import sys
import pymysql

def mydbConn():
    return pymysql.connect(host='localhost', user='root', password='1234', db='testdb', charset='utf8')


def screen():
    print("\n### 간단한 회원 관리 프로그램 ###")
    print("0.초기생성 1.멤버추가 2.멤버리스트 3.멤버찾기 4. 정보수정 5. 화면지우기 6.종료")


def memberAdd() :
    name = input("->이름: ")
    email = input("->이메일: ")
    age = input("->나이: ")

    conn = mydbConn()
    curs = conn.cursor()
    sql = """insert into member (email, name, age) values (%s, %s, %s)"""
    curs.execute(sql, (name,email,age))

    conn.commit()
    conn.close()

def memberAllList(memlist):
    print("\n-------- 정보 -----------")
    print("성명\t\t이메일\t\t\t나이")
    conn = mydbConn()
    curs = conn.cursor()
    sql = "select * from member"

    curs.execute(sql)
    rows = curs.fetchall()

    for row in rows:
         print(row[0],'\t', row[1], '\t', row[2]) #print(row['idx'], row['email'], row['age'])

    conn.close()

def memberSearch(memlist):
    ser_name = input("찾고하고 싶은 이름:  ")

    conn = mydbConn()
    curs = conn.cursor()
    sql = "select * from member where name=%s"

    curs.execute(sql, ser_name)
    rows = curs.fetchall()
    for row in rows:
        print(row[0],'\t', row[1], '\t', row[2])

    conn.close()

def memberModify(memlist):
    ser_name = input("찾고 싶은 이름:  ")
    conn = mydbConn()
    curs = conn.cursor()

    sql = "select * from member where name=%s"
    curs.execute(sql, ser_name)
    rows = curs.fetchall()
    for row in rows:
        print(row[0], '\t', row[1], '\t', row[2])

    modAge = input('변경 나이->')

    sql = """update member set age = %s
             where name = %s"""
    curs.execute(sql, (modAge, ser_name))
    #
    # #sql = "delete from customer where id=%s"
    # #curs.execute(sql, 6)
    #
    print("변경 되었음.")
    conn.commit()
    conn.close()

def createNodeInit():
    conn = mydbConn()
    curs = conn.cursor()
    sql = """insert into member (name, email, age) values (%s, %s, %s)"""
    curs.execute(sql, ('temp1', 'temp1@nate.com', '100'))
    curs.execute(sql, ('temp2', 'temp2@nate.com', '200'))
    conn.commit()
    print("초기 데이터 추가되었음.")
    conn.close()


if __name__ == '__main__' :
    memlist = []

    while True:
        screen()
        choice = input("-> ")

        if choice == "0":
           createNodeInit()
        elif choice == "1":
            memberAdd()
        elif choice == "2":
            memberAllList(memlist)
        elif choice == "3":
            memberSearch(memlist)
        elif choice == "4":
            memberModify(memlist)
        elif choice == "5" :
            os.system("cls")
        elif choice == "6":
            sys.exit(1)
        else:
            print("잘못된 번호! 다시 입력바랍니다.")


