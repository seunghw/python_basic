#10818번 최소, 최대
"""
import sys

bowl = []

a = int(sys.stdin.readline())

b = list(map(int,sys.stdin.readline().split()))

for i in range(a):

    bowl.append(b[i])

print(f"{min(bowl)} {max(bowl)}")
"""
#2562번 최댓값
"""
import sys
a = []


for i in range(9):
   
    a.append(int(sys.stdin.readline()))

print(max(a))
print(a.index(max(a)) + 1)
"""
#2577번 숫자의 개수
"""
import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

answer = a * b * c

answer = str(answer)

for i in range(10):

    print(answer.count(str(i)))

"""
#3052번 나머지
"""
import sys
a = []

for i in range(10):
    
    a.append(int(sys.stdin.readline()) % 42)

a = set(a) # 중복처리
print(len(a))
"""
#1546번 평균
"""
import sys

a = int(sys.stdin.readline())
 
score = list(map(float, input().split()))
 
max = 0
for i in range(a):
    if score[i] > max:
        max = score[i]
 
for i in range(a):
    score[i] = score[i]/max*100
 
sum = 0
for i in range(a):
    sum += score[i]
 
print(sum/a)
"""
#8958번 ox퀴즈
"""
import sys

case = int(sys.stdin.readline())

for i in range(case):
    b = sys.stdin.readline()
    arr = list(b)
    sum = 0
    score = 1
    for i in arr:
        if i == 'O':
            sum += score
            score += 1
        else:
            score = 1
    print(sum)
"""
#4344번 평균은 넘겠지

for i in range(int(input())):
    list_input = list(map(int,input().split()))
    avg = sum(list_input[1:]) / list_input[0]
    count = 0
    for j in list_input[1:]:
        if j > ave:
            count += 1
    print(str('%.3f' % round(count / list_input[0] * 100, 3)) + '%')







