def add():
    with open("file.txt", mode="a+") as fi:
        fi.readlines()
        print("Enter EmpID,Name,Gender,DOJ and Dept")
        eid = input()
        n = input()
        g = input()
        doj = input()
        dept = input()
        fi.write(f"{eid} {n} {g} {doj} {dept}" + "\n")


def view():
    with open("file.txt", mode="r") as fi:
        cont = fi.read()
        print(cont)


def edit():
    with open("file.txt", mode="r") as fi:
        fi.seek(0)
        x1 = fi.readlines()
    with open("file.txt", mode="w") as fi:
        w = input("Enter EmpId of which employee to change")
        for emp in x1:
            z = emp.split()
            if z[0] == w:
                index = int(input("Enter 1.Name 2.Gender,3.DOJ,4.Dept"))
                val = input("Enter value")
                z[index] = val
                x2 = " ".join(z) + "\n"
                print(x2)
                fi.writelines(x2)
            else:
                fi.writelines(emp)


def delete():
    with open("file.txt", mode="r") as fi:
        fi.seek(0)
        x1 = fi.readlines()
    with open("file.txt", mode="w") as fi:
        w = input("Enter EmpId of which employee to be deleted")
        for emp in x1:
            z = emp.split()
            if z[0] == w:
                pass
            else:
                fi.writelines(emp)


with open("file.txt", mode="w+") as f:
    x = f.readlines()
    f.write("EmpID Name Gender DOJ Dept : \n")

c = 0
while c != '5':
    c = input("Enter\t1.Add\t2.View\t3.Edit\t4.Delete\t5.Exit: ")
    match c:
        case '1':
            add()
        case '2':
            view()
        case '3':
            edit()
        case '4':
            delete()
