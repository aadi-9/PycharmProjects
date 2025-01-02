import sys
import os


def drink(w,m,c):
    cent = 0.01
    nickel = 0.05
    quarter = 0.25
    dime = 0.1
    if w<250 or c<24 or m<150:
        print("less resources.Refill")
        print(f"water={w},coffee={c},milk={m}")
        sys.exit()

    cup=input("what would you like(1-expresso 2-latte 3-cappuccino) or report: ")
    if cup == '1':
        print(f"Expresso costs $1.5")
        p=1.5
        w-=50
        c-=18
    elif cup == '2':
        print(f"Latte costs $2.5")
        p=2.5
        w-=200
        c-=24
        m-=150
    elif cup == '3':
        print(f"Cappuccino costs $3.0")
        p=3.0
        w-=250
        c-=24
        m-=100
    else:
        print(f"water={w},coffee={c},milk={m}")
        drink(w,m,c)
    ce=int(input("Enter no.of cents($0.01)-"))
    ni=int(input("Enter no.of nickel($0.05)-"))
    qu=int(input("Enter no.of quarter($0.25)"))
    di=int(input("Enter no.of dime($0.10)"))
    total=ce*cent+ni*nickel+qu*quarter+di*dime
    print(f"money received={total}")
    if total>=p:
        print(f"your change is={(total-p)}")
        print("Enjoy you drink!")
    else:
        print("Not enough money. Sorry:) ")
    y=input("Do u want one more drink")
    if y=='y':
        os.system('clear')
        drink(w, m, c)
    else:
        sys.exit()

drink(300,200,100)