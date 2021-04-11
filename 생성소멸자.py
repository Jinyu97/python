class Car:
    man=4
    def __init__(self, _man=4): #생성자는 객체 만들 때 자동 수행(c1, c2 만들때마다 수행하므로 init 2번 출력)
        print('init')
        self.man=_man
    def run(self):
        print('run')
    def __del__(self): #소멸자는 객체가 사라질 때 자동 수행
        print('del')

#자동차 생성과 동시에 4/6인용 결정
c1=Car(6)
c2=Car()

print(c1.man, c2.man)
