#list comprenhension

l1=[]
for i in range(1,10):  #1
    if i%2==1: #2
        l1.append(i)  #3

l2=[i for i in range(1,10) if i%2==1] #list 안이므로 append할 필요 없음 [3 1 2] 다수 줄x 한줄씩만
print(l1)
print(l2)