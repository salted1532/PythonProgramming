선택

aa=[8,31,48,73,3,65,20,29,11,15]

for i in range(0,9) :

    ss=aa[i]

    for j in range(i,9) : #제일 작은값 위치 찾기

        if ss >= aa[j+1] :

            ss=aa[j+1]

            sp = j+1

            if i < sp : # 제일 작은 값과 현재값 위치 교환

                st = aa[i]

                aa[i] = aa[sp]

                aa[sp] = st

print(aa)

버블

aa=[8,31,48,73,3,65,20,29,11,15]

 

for i in range(0,9) :

    print(aa)

    for j in range (0,9-i) :

        if aa[j] >= aa[j+1]:

            ss=aa[j]

            aa[j] = aa[j+1]

            aa[j+1] = ss

print(aa)

삽입

aa=[8,31,48,73,3,65,20,29,11,15]

 

for i in range(0,10):

    print(aa)

 

    for j in range(0,i) :

        if aa[j] >= aa[i] :

            ss = aa[j] # 해당 위치값 저장

            aa[j] = aa[i] # 해당 위치에 삽입

            

            for k in range(j+1, i+1):

                tt = aa[k] # 해당 위치 이후 값 한칸씩 밀기

                aa[k] = ss

                ss = tt

print(aa)