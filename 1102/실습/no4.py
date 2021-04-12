f4 = open('file2.txt', 'r')
for i in range(1,4):
    f4.seek(32*(i-1)+3*i, 0)
    temp=f4.readline()
    print(temp,end='')


