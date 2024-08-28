# db1.py

import sqlite3

#연결객체 생성
# con=sqlite3.connect(":memory:")
#파일에 저장
con=sqlite3.connect('c:\\work\\sample.db')

#SQL구문을 실행하는 커서 객체 생성
cur=con.cursor()
#테이블 구조 생성 (체크 코드 추가)
cur.execute("create table if not exists PhoneBook (Name text, PhoneNum text);")

#입력구문
cur.execute("insert into PhoneBook values ('derick', '010-111');")
#입력 매개변수 처리
name='전우치'
phoneNum = '010-1111'
cur.execute("insert into PhoneBook values (?, ?);", (name, phoneNum))
#다중행을 입력
datalist = (('이순신', '010-2222'), ('박문수', '010-3333'))
cur.executemany('insert into PhoneBook values (?, ?);', datalist)

#검색구문
cur.execute('select * from PhoneBook;')
for row in cur:
    print(row)
# print('---fetchone()---')
# print(cur.fetchone())
# print('---fetchmany(2)---')
# print(cur.fetchmany(2))
# print('---fetchall()---')
# print(cur.fetchall())

#정상적으로 완료(con객체) 안하면 저장안됨    
con.commit()