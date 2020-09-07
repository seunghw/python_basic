#2741번 N 찍기
"""
import sys


count = int(sys.stdin.readline())

for i in range(count):
    print(i+1)
"""
#2742번 기찍 N
"""
import sys

count = int(sys.stdin.readline())

for i in range(count):
    print(count)
    count-= 1
"""
#11021번 A + B - 7
"""
import sys

count = int(sys.stdin.readline())

for i in range(count):

    a,b = map(int,(sys.stdin.readline().split()))
    print(f"Case #{i+1}: {a+b}")
"""
#11022번 A+B-8
"""
import sys

count = int(sys.stdin.readline())

for i in range(count):

    a,b = map(int,sys.stdin.readline().split())

    print(f"Case #{i+1}: {a} + {b} = {a+b}")
"""
#2438번 별찍기
"""
import sys

number = int(sys.stdin.readline())

for i in range(0,number):
    print("*" * (i+1))
"""
#2439번 거꾸로 별찍기
"""
import sys

number = int(sys.stdin.readline())

for i in range(1,number+1):
    print(" "*(number-i) + "*"*i)
"""
#10871번
#X보다 작은 수
import sys

cup = []

n,x = map(int,sys.stdin.readline().split())

a = list(map(int,sys.stdin.readline().split()))

for i in range(n):
    if (a[i] < x):
       cup.append(a[i])
    else:
        None
print(*cup, sep = " ")
    
    





