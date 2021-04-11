class Car:
    man=4
    tire=4 #속성
    def run(self):
        print('run')
    def stop(self):
        print('stop') #메소드

c1=Car()
c2=Car()

print(c1.man, c2.man)
c1.run()
c2.run()

c1.man=6

print(c1.man, c2.man) #->c1, c2는 별개로 만들어진 것
