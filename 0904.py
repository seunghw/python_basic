#입출력과 사칙연산

"""
#1번 헬로월드

print("Hello World!")

#2번 육구니

double = [1,2]

for a in double:
    print("강한친구 대한육군")


#3번 고양이

print("\     /\ ")
print(" )   ( ')")
print("(   /  )")
print(" \ (__)|") 

#1000번 덧셈

a,b = map(int, input().split())
print(a+b)

#split 함수는 a.split()처럼 괄호 안에 
# 아무 값도 넣어 주지 않으면 공백(스페이스, 탭, 엔터 등)을 
# 기준으로 문자열을 나누어 준다.

#1001번 뺄셈

a,b = map(int, input().split())
print(a-b)

#10998번 곱셈

a,b = map(int, input().split())
print(a*b)

#1008번

a,b = map(int, input().split())
print(a/b)

#10869번

a,b = map(int, input().split())
print(a+b)
print(a-b)
print(a*b)
print(int(a/b))
print(a%b)

#10430번

a,b,c = map(int, input().split())

print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)

#2588번

a = int(input())
b = int(input())

print(a*(b%10))
print(a*((b%100) // 10))
print(a*(b//100))
print(a*b)

## // 연산자는 몫만 반환해준다.
## a = input() 이대로 저장하면 문자열형태로 저장됨
## a = int(input()) 이렇게 저장해야 정수형을 저장되어서 수를 활용가능.

"""


