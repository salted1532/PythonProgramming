print("%d / %d = %0.1f" % (100, 200, 111.555))

 

print("{2:d} {1:d} {0:d}".format(100, 200, 300))

myVar = 100

print(type(myVar))

myVar = 100.0

print(type(myVar))

 

print(bin(11))

print(oct(11))

print(hex(11))

 

def myFunc() :

    print("함수를 호출함")

 

gVar = 160

 

print('메인 함수 부분이 실행됩니다.')

myFunc()

print('전역 변수 값',gVar)

 

 

while True:

    sel = int(input("입력 진수 결정 16/10/8/2) : "))

    num = input("값 입력 : ")

 

    if sel == 16 :

        h = hex(int(num))

        print ((h)[2:])

    if sel == 10 :

        print((num)[2:])

    if sel == 8 :

        o = oct(int(num))

        print ((o)[2:])

    if sel == 2 :

        b = bin(int(num))

        print ((b)[2:])