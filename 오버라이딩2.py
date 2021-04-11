class T:
    i=5
    def __add__(self, other):
        temp=T()
        temp.i=self.i+other.i
        return temp
    
    def test(self):
        print('T')

class T2(T):
    def test(self):
        super().test() #부모의 test
        print('T2') #자식의 test

t1=T()
t2=T2()

t1.test()
t2.test() #부모의 test, 자식의 test 둘다 수행
