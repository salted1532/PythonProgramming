# PythonProgramming
파이썬프로그래밍 수업내용

2022-1학기-정영만-파이썬프로그래밍

| 항목 | 내용 |
|:----:|:-----|
| 🎓 과목명 | 파이썬프로그래밍 |
| 🏫 담당 교수 | 정영만 교수님 |
| 🗓️ 수강 학기 | 2022-1학기 |
| 💡 주요 학습 내용 | Python |
| 🧰 도구 | IDLE 편집기 |
| 🧩 과제 / 프로젝트 | 파이썬을 이용한 여러 알고리즘 문제 |
| 🔗 관련 자료 | [노트 보기](./notes/README.md) / [과제 코드](./assignments/) |
---
## 1. 파이썬 기초
### 1-1. 출력과 변수

- print() 함수로 출력

- 변수 선언과 자료형 확인 (int, float)

- 문자열 포맷팅 예시
```
# 숫자 계산과 출력
print("%d / %d = %0.1f" % (100, 200, 111.555))

# 문자열 포맷팅 예시
print("{2:d} {1:d} {0:d}".format(100, 200, 300))

# 변수와 자료형 확인
myVar = 100
print(type(myVar))  # <class 'int'>

myVar = 100.0
print(type(myVar))  # <class 'float'>
```
### 1-2. 진법 표현
- 2진수, 8진수, 16진수 변환
```
print(bin(11))  # 0b1011
print(oct(11))  # 0o13
print(hex(11))  # 0xb
```
### 1-3. 기본 연산과 입력

- 입력 받기 (input)
- 산술 연산
- 조건문과 BMI 계산
```
height = int(input("키:"))
weight = int(input("몸무게:"))

bmi = weight / ((height/100) ** 2)
print(bmi)

if bmi >= 25:
    print("비만")
elif bmi >= 23:
    print("과체중")
elif bmi >= 18.5:
    print("정상")
else:
    print("저체중")
```
---
## 2. 조건문과 반복문
### 2-1. 조건문 (if, elif, else)

- 성인/미성년자 판단

- BMI에 따른 분류
```
age = int(input("내 나이:"))
if age >= 20:
    print("성인입니다.")
else:
    print("미성년자입니다.")
```
### 2-2. 반복문 (for, while)

- for 반복문: 1~9 출력

- while 반복문: 무한 루프 및 종료 조건

- 반복문에서의 사용자 입력 처리
```
# 1~9 출력
for a in range(1,10):
    print(a)

# 무한 루프 예제 (16진수, 10진수 등 입력)
while True:
    sel = int(input("입력 진수 결정 16/10/8/2) : "))
    num = input("값 입력 : ")

    if sel == 16:
        print(hex(int(num))[2:])
    elif sel == 10:
        print(num)
    elif sel == 8:
        print(oct(int(num))[2:])
    elif sel == 2:
        print(bin(int(num))[2:])
```
---
## 3. 함수
### 3-1. 함수 정의와 호출

- 기본 함수 정의
```
def myFunc():
    print("함수를 호출함")

myFunc()
```
### 3-2. 재귀 함수

- 팩토리얼 계산
```
def fact(a):
    if a == 1:
        return 1
    return a * fact(a-1)

a = int(input("원하시는 팩토리얼 수:"))
print(fact(a))
```
---
## 4. 자료구조
### 4-1. 리스트

- 리스트 생성 및 인덱싱

- 반복문과 리스트 활용
```
aa = [8,31,48,73,3,65,20,29,11,15]
print(aa[0])  # 리스트 첫 번째 값 출력
```
### 4-2. 리스트 정렬 알고리즘

- 선택 정렬

- 버블 정렬

- 삽입 정렬

- 각 알고리즘의 특징과 구현 방법
```
선택 정렬
aa=[8,31,48,73,3,65,20,29,11,15]

for i in range(0,9):
    ss=aa[i]
    for j in range(i,9):
        if ss >= aa[j+1]:
            ss = aa[j+1]
            sp = j+1
            if i < sp:
                st = aa[i]
                aa[i] = aa[sp]
                aa[sp] = st

print(aa)
```
```버블 정렬
aa=[8,31,48,73,3,65,20,29,11,15]

for i in range(0,9):
    for j in range(0,9-i):
        if aa[j] >= aa[j+1]:
            ss = aa[j]
            aa[j] = aa[j+1]
            aa[j+1] = ss

print(aa)
```
```삽입 정렬
aa=[8,31,48,73,3,65,20,29,11,15]

for i in range(0,10):
    for j in range(0,i):
        if aa[j] >= aa[i]:
            ss = aa[j]
            aa[j] = aa[i]
            for k in range(j+1, i+1):
                tt = aa[k]
                aa[k] = ss
                ss = tt

print(aa)
```
---
## 5. 모듈과 라이브러리 활용
### 5-1. 랜덤과 시간

- random 모듈로 난수 생성

- time 모듈로 시간 측정
```
import random
import time

stime = time.time()
r = random.random()
g = random.random()
b = random.random()
print("랜덤 색상 값:", r, g, b)

print("경과 시간:", time.time() - stime)
```
### 5-2. Turtle 그래픽

- 거북이를 이용한 그래픽

- 무작위 이동, 색상 설정

- 화면 범위를 벗어나면 초기화

- 게임/시뮬레이션 활용 가능
```
import turtle
import random

turtle.title('거북이가 맘대로 다니기')
turtle.shape('turtle')
turtle.pensize(3)
turtle.setup(530, 530)
turtle.screensize(500, 500)

for _ in range(5):
    r, g, b = random.random(), random.random(), random.random()
    turtle.pencolor((r,g,b))
    turtle.left(random.randrange(0,360))
    turtle.forward(random.randrange(1,100))

turtle.done()
```
---
## 6. GUI 프로그래밍 (Tkinter)
```6-1. 사진 앨범
from tkinter import *

fnameList = ["jeju1.gif", "jeju2.gif", "jeju3.gif"]
num = 0

def clickNext():
    global num
    num = (num + 1) % len(fnameList)
    photo = PhotoImage(file=fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image = photo

def clickPrev():
    global num
    num = (num - 1) % len(fnameList)
    photo = PhotoImage(file=fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image = photo

window = Tk()
window.geometry("700x500")
window.title("사진 앨범 보기")

btnPrev = Button(window, text="<< 이전", command=clickPrev)
btnNext = Button(window, text="다음 >>", command=clickNext)
photo = PhotoImage(file=fnameList[0])
pLabel = Label(window, image=photo)

btnPrev.place(x=250, y=10)
btnNext.place(x=400, y=10)
pLabel.place(x=15, y=50)

window.mainloop()
```
```6-2. 3x3 이미지 버튼
from tkinter import *

btnList = [""] * 9
fnameList = ["froyo.gif", "gingerbread.gif", "honeycomb.gif"]
photoList = [None] * 9
num = 0

window = Tk()
window.geometry("210x210")

for i in range(3):
    photoList[i] = PhotoImage(file=fnameList[i])
    btnList[i] = Button(window, image=photoList[i])

xPos, yPos = 0, 0
for i in range(1):
    for k in range(3):
        btnList[num].place(x=xPos, y=yPos)
        num += 1
        xPos += 70
    xPos = 0
    yPos += 70

window.mainloop()
```
