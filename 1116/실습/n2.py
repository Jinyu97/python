class point:
    def __init__(self,_x=0,_y=0):
        self.x=_x
        self.y=_y
    def __add__(self,other):
        temp=point()
        temp.x=self.x+other.x
        temp.y=self.y+other.y
        return temp

class point3d(point):
    def __init__(self,_x=0,_y=0,_z=0):
        point.__init__(self,_x,_y)
        self.z=_z
    def __add__(self,other):
        temp=point3d()
        temp.x = self.x + other.x
        temp.y = self.y + other.y
        temp.z=self.z+other.z
        return temp

p1=point3d(int(input()),int(input()),int(input()))
p2=point3d(int(input()),int(input()),int(input()))
p3=p1+p2
print(p3.x,p3.y,p3.z)

