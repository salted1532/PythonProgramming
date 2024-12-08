# num1, num2 = 511, 512
# print(num1+num2)

# num1, num2 = num2, num1
# print(num1)
# print(num2)

# for a in range(1,10):
#     print(a)


# age = int(input("내나이:"))
# if age >= 20:
#     print("성인입니다.")
# else:
#     print("미성연자입니다.")
    

# height = int(input("키:"))
# weight = int(input("몸무게:"))

# bmi = weight/((height/100)*(height/100))
# print(bmi)
# if bmi >= 25:
#     print("비만")
# elif bmi >= 23:
#     print("과체중")
# elif bmi >= 18.5:
#     print("정상.")
# elif bmi <= 18.5:
#     print("저체중")   

def fact(a):
    if a == 1:
        return 1
    return a * fact(a-1)

a = int(input("원하시는 팩토리얼 수:"))

print(fact(a))


