class point3d():
    def __init__(self,_x=0,_y=0,_z=0):
        self.x = _x
        self.y = _y
        self.z=_z
    def __add__(self,other):
        temp=point3d()
        temp.x = self.x + other.x
        temp.y = self.y + other.y
        temp.z=self.z+other.z
        return temp

class pointt(point3d):
    def maximum(self,other):
        temp=point3d()
        temp.x=max(self.x,other.x)
        temp.y = max(self.y, other.y)
        temp.z = max(self.z, other.z)
        return temp

p1=pointt(int(input()),int(input()),int(input()))
p2=pointt(int(input()),int(input()),int(input()))

p3=p1.maximum(p2)
print(p3.x,p3.y,p3.z)