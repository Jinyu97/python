str1=input()
f1=open('test.txt','w+')
list1=str1.split()
for temp in list1:
    f1.write(temp+'\n')

f1.seek(0,0)
for temp in f1:
    print(temp,end='')

f1.close()