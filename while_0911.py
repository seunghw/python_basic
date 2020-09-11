#10952번 A+B - 5
"""
import sys

while True:

    try:
        a,b = map(int,sys.stdin.readline().split())
        print(a+b)
    except:
        break

"""
#1110번 더하기 사이클
import sys


t = int(sys.stdin.readline())
times = 0
b = t
a = 0

while True:
    times += 1   
    ten = t // 10 
    one = t % 10
    summ = ten + one

    a = one * 10 + (summ % 10)
    t = a
    if a == b:
        break
print(times)


        




        
        


