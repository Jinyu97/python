class point:
    def __init__(self,_x=0,_y=0, _z=0):
        self.x=_x
        self.y=_y
        self.z = _z
    def equal(self,other):
        if (self.x==other.x and self.y==other.y and self.z==other.z):
            print('eq')
        else:
            print('not eq')

p1=point(int(input()),int(input()),int(input()))
p2=point(int(input()),int(input()),int(input()))

p1.equal(p2)
