
import random
while True:
    Setnumber = random.randint(0,100)
    #print(Setnumber)
    Guessnumber = int(input("请输入猜测的数(1~100):"))
    N = 1
    while(Guessnumber < Setnumber or Guessnumber > Setnumber):
        N = N + 1
        if Guessnumber > Setnumber:
            print("大了")
        elif Guessnumber < Setnumber:
            print("小了")
        Guessnumber = int(input("请重新输入猜测的数(1~100):"))
    print("猜对了，猜了",N,"次")
