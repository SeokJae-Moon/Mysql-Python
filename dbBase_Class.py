import os
import sys
import pymysql

class Member:
    def __init__(self):
        self.__name = ''
        self.__email = ''
        self.__major = ''
        
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def email(self):
        return self.email
    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def major(self):
        return self.major
    @major.setter
    def major(self, major):
        self.__major = major

def mydbConn():
    return pymysql.connect(host='localhost', user='root', password='1234', db='world', charset='utf8')

def screen():
    print("\n### DB기반의 클래스를 이용한 회원 관리 프로그램 ###")
    print("  1.회원추가 2.회원목록 3.회원검색 4.회원정보수정 5.화면지우기 6.종료 ")

def createMember():
    name = input("->이름: ")        
    email = input("->이메일: ")        
    major = input("->전공: ")

    member = Member()
    member.__name = name
    member.__email = email
    member.__major = major
        
    conn = mydbConn() 
    try:
        with conn.cursor() as curs:
            sql = "insert into member (name, email, major) values (%s, %s, %s)"
            curs.execute(sql, (member.__name, member.__email, member.__major))
        conn.commit()
        print("%s님이 추가되었음!" % (name))
    finally:
        member = pymysql.NULL
        conn.close()    

def memberAllList():
    print("\n--------------- 정보 ----------------------------------")
    print("ID\t성명\t\t이메일\t\t\t전공")
    print("-------------------------------------------------------")
    conn = mydbConn()
    curs = conn.cursor()
    member = Member()

    try:
        with conn.cursor() as curs:
            sql = "select * from member"
            curs.execute(sql)
            rows = curs.fetchall()
            
            for row in rows:
                id = row[0]                
                member.__name = row[1]
                member.__email = row[2]
                member.__major = row[3]
                print(id,'\t',  member.__name, '\t', member.__email, '\t', member.__major) 
    finally:
        member = pymysql.NULL
        conn.close()

def memberSearch():
    ser_name = input("찾고하고 싶은 이름:  ")
    conn = mydbConn()
    member = Member()

    print("-------------------------------------------------------")
    print("ID\t성명\t\t이메일\t\t\t전공")    
    try:
        with conn.cursor() as curs:
            sql = "select * from member where name=%s"
            curs.execute(sql, ser_name)
            rows = curs.fetchall()
            for row in rows:
                id = row[0]                
                member.__name = row[1]
                member.__email = row[2]
                member.__major = row[3]
                print(id,'\t',  member.__name, '\t', member.__email, '\t', member.__major) 
    finally:
        member = pymysql.NULL
        conn.close()
    print("-------------------------------------------------------")

def memberModify():
    ser_name = input("찾고 싶은 이름:  ")
    conn = mydbConn()
    member = Member()

    try:
        with conn.cursor() as curs:
            sql = "select * from member where name=%s"
            curs.execute(sql, ser_name)
            rows = curs.fetchall()
            for row in rows:
                id = row[0]                
                member.__name = row[1]
                member.__email = row[2]
                member.__major = row[3]
                print(id,'\t',  member.__name, '\t', member.__email, '\t', member.__major) 

        modEmail = input('변경 이메일-> ')
        modMajor = input('변경 전공-> ')
        with conn.cursor() as curs:
            sql = "update member set email=%s, major=%s where name = %s"
            curs.execute(sql, (modEmail, modMajor, ser_name))

        conn.commit()
        print("%s님 정보가 변경되었음!" % (ser_name))
    finally:
        member = pymysql.NULL
        conn.close()

if __name__ == '__main__' :
    memlist = []

    while True:
        screen()
        choice = input("-> ")

        if choice == "1":
            createMember()
        elif choice == "2":
            memberAllList()
        elif choice == "3":
            memberSearch()
        elif choice == "4":
            memberModify()
        elif choice == "5" :
            os.system("cls")
        elif choice == "6":
            sys.exit(1)
        else:
            print("잘못된 번호! 다시 입력바랍니다.")

# CREATE TABLE `member` (
#   `id` int(11) NOT NULL AUTO_INCREMENT,
#   `name` varchar(200) DEFAULT NULL,
#   `email` varchar(200) DEFAULT NULL,
#   `major` varchar(200) DEFAULT NULL,
#   PRIMARY KEY (`id`)
# ) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
