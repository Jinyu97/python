class cc1:
    x=5
    def __init__(self):
        print('cc1 init')
    def test(self):
        print('cc1 test')
    def __del__(self):
        print('cc1 del')

class cc2(cc1):
    y=5
    def __init__(self):
        super().__init__() #부모의 함수 호출
        print('cc2 init')
    def test(self):
        super().test()
        print('cc2 test')
    def __del__(self):
        print('cc2 del')

o1=cc1()
o2=cc2()
print(o1.x, o2.x, o2.y)
o1.test()
o2.test()

o3=o2
o4=o2.xcopy() #????
o2.x=99
print(o2.x, o3.x, o4.x)