class car:
    man=4
    tire=4
    def run(self):
        print('run')

class sedan(car):
    comport=100
    def run(self):
        print('sedan run')
    def __add__(self,other): #1. 자기 자신에 다른 것을 더하므로 other 추가
        temp=sedan()  #2. 두 자동차 더해서 새로운 자동차
        temp.comport=self.comport+other.comport #2.
        return temp #2.
        #1. self.comport=self.comport+other.comport

c1=car()
c2=sedan()
c3=sedan()

print(5+6)
#c2+c3   #1.c2에 c3을 더함
c4=c2+c3 #2. 자동차 2개 더한 새로운 자동차.

#print(c2.comport)  2.c2의 comport+c3의 comport 값 나옴
print(c4.comport)
