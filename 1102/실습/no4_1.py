f4 = open('file2.txt', 'r')

num=1
for i in f4: #i:파일의 line 1개
    print(i[3*num:],end='')
    num+=1