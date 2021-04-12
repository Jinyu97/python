f1=open('test1.txt','w')
for i in range(1,6):
    f1.write('%3d lines\n'%i)

f1.close()

f2 = open('test1.txt', 'r')
for temp in f2:
    print(temp, end='')
    print(type(temp))

#temp=f2.readline()
#print(temp, end='')
f2.close()