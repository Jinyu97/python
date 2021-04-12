f3=open('file2.txt','w')
for i in range(1,11):
    data='%3d'%i
    f3.write(data)
f3.write('\n')
for i in range(11,21):
    data='%3d'%i
    f3.write(data)
f3.write('\n')
for i in range(21,31):
    data='%3d'%i
    f3.write(data)
f3.write('\n')