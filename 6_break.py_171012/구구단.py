#구구단
for j in range(1,10):
    for i in range(2,10):
        print('%d*%d=%2d '%(i,j,i*j),end='')
    print()
print()

#역으로 출력
for j in range(9,0,-1):
    for i in range(2,10):
        print('%d*%d=%2d '%(i,j,i*j),end='')
    print()
print()

#3,5,7,9단만 출력
for j in range(1,10):
    for i in range(3,10,2):
        print('%d*%d=%2d '%(i,j,i*j),end='')
    print()