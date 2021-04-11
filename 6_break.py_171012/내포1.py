#list comprenhension

l1=[]
for i in range(1,10):  #1
    l1.append(i)  #2

l2=[i for i in range(1,10)] #list 안이므로 append할 필요 없음 [2 1]
print(l1)
print(l2)