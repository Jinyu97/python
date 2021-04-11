str1="ABCDEF"
c=str(input('구분기호 입력하세요.'))
print(c)
d=c.join(str1)
print(d)
print(d.split(c))
