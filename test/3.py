d1={1:95,2:100,3:110,4:130}
d2={1:1.10,2:1.20,3:0.95,4:0.8}
num1=int(input())
num2=int(input())
num3=int(input())
import math
for i in range (1,num3+1):
    ty1=d1[num1]*d2[i]
    ty2=d1[num2]*d2[i]
print(math.floor(ty1),math.floor(ty2),math.floor(ty1-ty2))