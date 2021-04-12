def equation(fx1, fy1, fx2, fy2):
    if fx1!=fx2:
        fm=(fy2-fy1)/(fx2-fx1)
        fc=fy1-fm*fx1
        return fm,fc
    else:
        return 0


x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())

m,c=equation(x1,y1,x2,y2)
if x1!=x2:
    print('y=%8.2fx+%8.2f' % (m, c))
else:
    print('x=%d'%x1)