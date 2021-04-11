str1=input()
d1={'a':7, 'b':9, 'c':11, 'd':13, 'e':3, 'f':20, 'g':5, 'h':30, 'i':2, 'j':5}
mean=(str1.count('a')*d1.get('a')+str1.count('b')*d1.get('b')+str1.count('c')*d1.get('c')+str1.count('d')*d1.get('d')+str1.count('e')*d1.get('e')+str1.count('f')*d1.get('f')+str1.count('g')*d1.get('g')+str1.count('h')*d1.get('h')+str1.count('i')*d1.get('i')+str1.count('j')*d1.get('j'))/len(str1)

import math
print(math.ceil(mean))
