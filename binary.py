import turtle

## 전역 변수 선언 부분 ##
num = 0 
swidth, sheight= 1000, 300
curX, curY = 0, 0

## 메인 코드 부분 ##
if __name__ == "__main__" :
    turtle.title('거북이로 두 숫자 비트 논리합(|) 연산하기')
    turtle.shape('turtle')
    turtle.setup(width=swidth+50, height=sheight+50)
    turtle.screensize(swidth, sheight)
    turtle.penup()
    turtle.left(90)

    num1=int(input("2진수를 입력하세요 : "), 2)
    num2=int(input("2진수를 입력하세요 : "), 2)
    num3= num1 | num2

 
    binary = bin(num1)
    curX = swidth / 2
    curY = 100
    # print(num1)
    # print(len(num1))
    # print(binary)
    # print(len(binary))
    for i in range(len(binary)-2) :
        turtle.goto( curX, curY )
   #     print(num1&1)
        if num1 & 1 :
            turtle.color('red')
            turtle.turtlesize(2)
        else :
            turtle.color('blue')
            turtle.turtlesize(1)
        turtle.stamp()
        curX -= 50
        num1 >>= 1
        
    binary = bin(num2)
    curX = swidth / 2
    curY = 0

    for i in range(len(binary)-2) :
        turtle.goto( curX, curY )
        if num2 & 1 :
            turtle.color('red')
            turtle.turtlesize(2)
        else :
            turtle.color('blue')
            turtle.turtlesize(1)
        turtle.stamp()
        curX -= 50
        num2 >>= 1

    binary = bin(num3)
    curX = swidth / 2
    curY = -100
    for i in range(len(binary)-2) :
        turtle.goto( curX, curY )
        if num3 & 1 :
            turtle.color('red')
            turtle.turtlesize(2)
        else :
            turtle.color('blue')
            turtle.turtlesize(1)
        turtle.stamp()
        curX -= 50
        num3 >>= 1
 
    turtle.done()
