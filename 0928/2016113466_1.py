s1=set(input())
s2=set(input())

key=list((s1|s2)-(s1&s2))
key.sort()
print(key)
