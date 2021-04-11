x=int(input()) #price
y=int(input()) #money

gm=y-x

mm=gm//10000
gm%=10000
print(mm)

mm=gm//5000
gm%=5000
print(mm)
mm=gm//1000
gm%=1000
print(mm)
mm=gm//500
gm%=500
print(mm)
mm=gm//100
gm%=100
print(mm)
mm=gm//10
gm%=10
print(mm)

