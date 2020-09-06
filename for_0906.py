#2739번
"""
a = int(input())

for i in range(1,10):
    print(f"{a} * {i} = {a*i}")

"""
#10950번
"""
count = int(input())
list = {}

for i in range(0,count):
    a,b = map(int, input().split())
    list[i] = a+b

for i in range(0,count):
    print(list[i])
"""
"""
#8393번 합

count = int(input())
sum = 0

for i in range(0,count+1):
    sum = i + sum

print(sum)
"""
"""
#15552번 빠른 A+B
import sys

count = int(sys.stdin.readline())
list = {}

for i in range(0,count):
    a,b = map(int, input().split())
    list[i] = a+b

for i in range(0,count):
    print(list[i])
"""
import sys

count=int(sys.stdin.readline())
for i in range (count):
    A,B=map(int, sys.stdin.readline().split())
    print(A+B)
