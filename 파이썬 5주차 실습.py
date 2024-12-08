1.  거북이가 맘대로 다니기

import turtle

import random

import time

 

stime = time.time()

 

swidth, sheight,pSize,exitCount = 500, 500, 3, 0

r, g, b, angle, dist, curX, curY = [0] * 7

 

turtle.title('거북이가 맘대로 다니기')

turtle.shape('turtle')

turtle.pensize(pSize)

turtle.setup(swidth + 30, height = sheight + 30)

turtle.screensize(swidth, sheight)

 

print(exitCount + 1,"번 거북이")

 

while True :

    r = random.random()

    g = random.random()

    b = random.random()

    turtle.pencolor((r,g,b))

 

    angle = random.randrange(0,360)

    dist = random.randrange(1,100)

    turtle.left(angle)

    turtle.forward(dist)

    curX = turtle.xcor()

    curY = turtle.ycor()

    survtime = time.time() - stime

    print("생존시간 :", int(survtime))

    

    if(-swidth / 2 <= curX and curX <= swidth / 2) and (-sheight / 2 <= curY and curY <= sheight / 2):

        pass

    else :

        turtle.penup()

        turtle.goto(0,0)

        turtle.pendown()

        stime = time.time()

 

        exitCount += 1

        print(exitCount + 1,"번 거북이")

        if exitCount >= 5 :

            break

 

turtle.done()

 

2. 증가 값 만큼 두 수 사이를 더하는 프로그램

answer, numStr, num1, num2, num3 = 0, "", 0, 0, 0

 

num1 = int(input("*** 첫번째 숫자를 입력하세요 : "))

num2 = int(input("*** 두번째 숫자를 입력하세요 : "))

num3 = int(input("*** 더할 숫자를 입력하세요 : "))

for i in range(num1, num2 + 1, num3) :

    answer = answer + i

print("%d+...+%d는 %d입니다." % (num1,num2,answer))