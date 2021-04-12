import random

class Car:
    man=4 #멤버 변수 만드는 법 1
    tire=4
    def __init__(self,_man=4,_tire=4):   #디폴트 매개변수
        self.man=_man
        self.tire=_tire
        print('init leeda')
    def __del__(self):   #소멸자
        print("del leeda")
    def run(self,_vel):
        self.vel=_vel #3
        print('run %4d'%self.vel)
    def stop(self):
        self.vel=0
        print('stop %4d'%self.vel)

obj1=Car()
car2=Car(5,6)

print(obj1.man, obj1.tire)

obj1.run(100)
obj1.stop()

del obj1
del car2

#obj1.vel=0 #2
#print(obj1.vel)
