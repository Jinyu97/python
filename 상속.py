class co:
    i=4
    def __init__(self, _i=4):
        self.i=_i
    def isco(self):
        print('co')

class co2(co): #상속
    j=8
    def __init(self, _i=4, _j=8):
        super(co2,self).__init__(_i) #self. 쓰지않음(함수 만드는게 아니라 호출하는것이므로)
        self.j=_j
    def isco2(self):
        print('co2')

c1=co(9)
c2=co2(11,22)
    
#print(dir(c1))
#print(dir(c2)) #c1, c2가 가진 속성 보여주는 함수. c2는 c1의 모든것+isco2, j 가짐

print(c1.i, c2.i)
#print(c1.j, c2.j) : 에러



