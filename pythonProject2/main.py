import sys
import pymysql as sql

con = sql.connect(user="python",password="Mysql@aadya",host="192.168.75.128",database="student")


def insert():
    ide = int(input("Enter \nEmployee id: "))
    name = input("Name: ")
    gender = input("gender: ")
    date = input("DOJ: ")
    dept = input("Department: ")
    cur = con.cursor()
    qry = "insert into empinfo values(%d,'%s','%s','%s','%s')"%(ide, name, gender, date, dept)
    cur.execute(qry)
    con.commit()
    if cur.rowcount == 1:
        print("Record Inserted")
    else:
        print("Error in inserting")


def delete():
    ide = int(input("Enter Employee id to be deleted: "))
    qry = f"delete from empinfo where eid={ide}"
    cur = con.cursor()
    cur.execute(qry)
    con.commit()
    if cur.rowcount == 1:
        print("Record Deleted")
    else:
        print("Error in deleting")


def update():
    ide = int(input("Enter \nEmployee id: "))
    cur = con.cursor()
    cur.execute(f"select * from empinfo where eid='{ide}'")
    if cur.rowcount == 1:
        name = input("Name: ")
        gender = input("gender: ")
        date = input("DOJ: ")
        dept = input("Department: ")
        qry = f"UPDATE empinfo SET name='{name}', gender='{gender}', doj='{date}', dept='{dept}' WHERE eid='{ide}'"
        cur.execute(qry)
        con.commit()
    else:
        print("Invaid eid")

def display():
    qry = "select * from empinfo"
    cur = con.cursor()
    cur.execute(qry)
    if cur.rowcount != 0:
        # print(cur.fetchone())
        # print(cur.fetchone())
        # print(cur.fetchone())
        for i in cur.fetchmany(3):
            print(i)
    else:
        print("Not found")


while True:
    x = input("Enter 1-Insert 2-Delete 3-Update 4-Display 5-exit : ")
    match x:
        case '1':
            insert()
        case '2':
            delete()
        case '3':
            update()
        case '4':
            display()
        case '5':
            con.close()
            sys.exit()
        case _:
            print("Invalid Choice")
