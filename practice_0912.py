#10039번 평균 점수
"""
import sys

SUM = 0
AVE = 0
for i in range(5):

    a = int(sys.stdin.readline())
    if(a < 40):
        a = 40
    
    SUM = SUM + a

AVE = SUM / 5

print(int(AVE))
"""
#5543번 상근날드
"""
import sys

bur = []
coke = []

for i in range(3):
    
    bur.append(int(sys.stdin.readline()))

for i in range(2):
    
    coke.append(int(sys.stdin.readline()))    
   
print(min(bur) + min(coke) - 50)
"""
#10817번 세 수
"""
import sys

lis = []

a = list(map(int,sys.stdin.readline().split()))

for i in range(3):

    lis.append(a[i])
a.sort()
print(a[1])
"""
#2523번 별찍기 - 13
"""
import sys

a = int(sys.stdin.readline())

for i in range(a):
    print("*" * (i+1))
for i in range(a-1,0,-1):
    print("*" *i)
"""
#2446번 별찍기 - 9

import sys

a = int(sys.stdin.readline())
count = (2 * a) - 1
j = 0
for i in range(count,0,-2):
    print(" " * j + "*" * i)
    j += 1



for i in range(3,count+1,2):
    print(" " * (j-2)  + "*" * i)
    j -= 1


