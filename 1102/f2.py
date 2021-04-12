import sys

f5=open('file3.txt','w+')
for i in range(1,101):
    data='%3d lines\n'%i
    f5.write(data)
f5.seek(0,0)
length=len(data)
x=int(input())
if sys.platform == 'win32':
    f5.seek((length+1)*(x-1),0)
else:
    f5.seek(length*(x-1),0)

print(f5.readline())