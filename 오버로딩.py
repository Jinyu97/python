class T:
    i=5
    #def __add__(self,other):
    #    self.i=self.i+other.i

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

print(t1.i, t2.i)

#t1+t2 
#print(t1.i) #t1 값이 바뀜

t3=t1+t2
print(t3.i)
print(t1.i, t2.i) #t1값 안 바뀜
