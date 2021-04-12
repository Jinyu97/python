x=int(input())
y=int(input())
while y!=0:
    r=x%y
    x,y=y,r  #y를 x에, r을 y에 저장. r(나머지)=0이 되면 반복문 종료하고 x 출력
print(x)