ss=input()
numList='0123456789'
l1=[int(ch) for ch in ss if (ch in numList)]
l2=[ch for ch in ss if not (ch in numList)]

l2.reverse()
print(sum(l1),l2)
