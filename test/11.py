a=int(input())
b=int(input())

for i in range(a,0,-1):
    for k in range (i-1):
        print('    ', end='')
    for j in range(1,b-i+2):
        print('%4d' %(i*100+j), end='')
    print()