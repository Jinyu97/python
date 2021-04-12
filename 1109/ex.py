f=open("새파일.txt",'w+')
for i in range(10,51,10):
    data="%2d lines\n"%i
    f.write(data)

f.seek(0,0)
for line in f:
    print(line, end='')

f.seek(0,0)
temp=f.readlines()
str1=[]
for a in temp:
    str1.append(a.strip('\n'))

print(str1)


f.seek(0,0)
print(f.read(),end='')

#temp=f.readline() #while문으로 반복
#print(temp,end='')

f.close()


