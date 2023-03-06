#1
'''
import math
a = input().split()
b = list(map(int, a))
c = math.prod(b)
print(c)

#2
a = 'ASDFhv cbdsljiaPOO'
count, count1 =0, 0
for i in a:
    if i.isupper():
        count +=1
    if i.islower():
        count1 +=1
print(count, count1)

#3
a = input()
b = ''.join(reversed(a))
if a == b:
    print(1)
else:
    print(0)

#5
a = input().split()
b = tuple(a)
print(all(b))'''

#4
