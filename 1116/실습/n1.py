class point:
    x=0
    y=0
    def __add__(self,other):
        temp=point()
        temp.x=self.x+other.x
        temp.y=self.y+other.y
        return temp

if __name__=='__main__':
    p1 = point()
    p2 = point()
    p1.x = int(input())
    p1.y = int(input())
    p2.x = int(input())
    p2.y = int(input())
    p3 = p1 + p2
    print(p3.x, p3.y)