str1=input()
temp=str1.split()

f1=open('file1.txt','w')
for str2 in temp:
    f1.write(str2+'\n')

f1.close()

