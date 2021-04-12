import sys
f3=open('test3.txt','w+')

for temp in range (1,101):
    f3.write('%3d lines\n'%temp)

num=int(input())

if sys.platform=='win32':
    count=len('100 lines\n')+1

else:
    count=len('100 lines\n')

f3.seek(count*(num-1),0)
print(f3.readline(),end='')

f3.close()
