f1=open('test1.txt','w')
for i in range(1,6):
    f1.write('%3d lines\n'%i)

f1.close()

f2 = open('test1.txt', 'r')
#read():파일 전체를 string으로 읽음, readline():한줄만 string으로 읽음, readlines():한줄한줄을 list의 원소로 읽음

temp=f2.read()
#temp=f2.readline()
# temp=f2.readlines()
print(type(temp))
print(temp,end='')
f2.close()