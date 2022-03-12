
A=input("输入9个随便什么东西，数字英文汉字，不足用空格代替")

l2=[]
for y in range(15,-15,-1):
    l3 = []
    for x in range(-30,30):
        l3.append((A[(x-y)%9]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' '))
    l2.append(''.join(l3))
l1 ='\n'.join(l2)

for i in l1:
    print("\033[91m"+i,end="",flush=True)