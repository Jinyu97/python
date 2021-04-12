import n1

class point3d(n1.point):
    z=0
    def __add__(self, other):
        temp=point3d()
        temp.z=self.z+other.z
        return temp

p1=point3d()
p2=point3d()
p1.x = int(input())
p1.y = int(input())
p1.z = int(input())
p2.x = int(input())
p2.y = int(input())
p2.z = int(input())
p3=p1+p2
print(p3.x,p3.y,p3.z)

