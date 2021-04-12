l1=[1,2,3]
l2=[10,20,30]

l3=l2
l4=l2.copy()

l2[0]=99

print(l2[0],l3[0])
print(l4[0])