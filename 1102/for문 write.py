f1=open('test.txt','w')
for i in range(1,6):
    f1.write('%3d lines\n'%i)

f1.close()