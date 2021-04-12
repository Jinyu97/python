f2=open('test2.txt','w+')
for temp in range(1,31):
    f2.write('%3d'%temp)
    if (temp%10==0):
        f2.write('\n')

f2.seek(0,0)
count=0
for temp in range(3,10,3):
    f2.seek(count+temp,0)
    print(f2.readline(), end='')
    count=f2.seek(0,1)

f2.close()