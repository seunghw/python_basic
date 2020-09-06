#IF문
#1330번
"""
a,b = map(int,input().split())

if a > b:
    print(">")
elif a < b:
    print("<")
else:
    print("==")

#9498번

a = int(input())

if a>=90:
    print("A")
elif a>=80: 
    print("B")
elif a>=70: 
    print("C")
elif a>=60: 
    print("D")
else:
    print("F")


#2753번 윤년

a = int(input())

if a % 4 == 0 and (a % 400 == 0 or a % 100 != 0 ):
    print("1")
else: 
    print("0")

#14681번 사문면 고르기

a = int(input())
b = int(input())

if a>0 and b>0:
    print("1")
elif a>0 and b<0:
    print("4")
elif a<0 and b>0:
    print("2")
else:
    print("3")

#2884번 알람시계

a,b = map(int, input().split())

if b - 45 >= 0:
    print(f"{a} {b-45}")
elif b - 45 < 0:
    if(a == 0):
        print(f"{a+23} {b+15}")
    else:
        print(f"{a-1} {b+15}")
"""
    



