f1=open('test2.txt','w+')

f1.write('123456789\n')
f1.write('abcdefghi\n')
f1.seek(0,0)
temp=f1.readline()
print(temp,end='')

f1.close()