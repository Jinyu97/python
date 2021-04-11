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
        print('T2')

t1=T()
t2=T2()

t1.test()
t2.test() #부모의 test위에 자식의 test가 올라가므로 부모의 test 실행 안함
