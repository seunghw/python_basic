# python_basic

파이썬을 공부하기위해서 baekjoon에 있는 단계별 알고리즘 문제를 이곳에 차근차근
옮겨 놓고 새로 배운 것들을 기록할 것 입니다.

day0904~0905

level 1 입출력과 사칙연산

## split 함수는 a.split()처럼 괄호 안에 
아무 값도 넣어 주지 않으면 공백(스페이스, 탭, 엔터 등)을 
기준으로 문자열을 나누어 준다.

## // 연산자는 몫만 반환해준다.
a = input() 이대로 저장하면 문자열형태로 저장됨
a = int(input()) 이렇게 저장해야 정수형을 저장되어서 수를 활용가능.

level 2 if문

## 추가할게 없어서 생략합니다.

level 3 for문

## range()
범위라는 뜻인데 어떤 정수를 인자로 주면 그 범위 안의 정수들을 만들어줌.
range(2,7) = 2
ex) for i in range(0,10) 
 >> 0부터 10미만인 9까지 반복

## sys.stdin.readline
Python에서 입력값을 받을 때 input() 함수를 사용하지만 시간단축을 위해 sys.stdin.readline을 사용한다.

num = int(input())   ->  num = int(sys.stdin.readline())

사용 시, import sys  선언 필요


여러 라인 입력 받을 경우 아래와 같이 사용하는 게 빠르다고 함.

n = input()
a = [sys.stdin.readline() for i in range(n)]

## sys.stdin: 

여러 줄 입력 받을 때

for line in sys.stdin:
    print(line)