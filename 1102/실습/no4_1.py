f4 = open('file2.txt', 'r')

num=1
for i in f4: #i:νμΌμ line 1κ°
    print(i[3*num:],end='')
    num+=1