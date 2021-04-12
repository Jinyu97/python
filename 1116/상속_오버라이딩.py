class car:
    man=4
    tire=4
    def run(self):
        print('run')

class sedan(car):
    comport=100
    def run(self):
        print('sedan run')

c1=car()
print(c1.man)
# print(c1.comport) #아버지는 아들에 접근 못함
c1.run()

c2=sedan()
print(c2.comport, c2.man) #아들은 자신의 것, 아버지 것 둘다 접근됨
c2.run()