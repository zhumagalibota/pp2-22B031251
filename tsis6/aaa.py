
def gen():
    n = 100
    for v in range(n):
        if v%2==0:
            yield v
            v = v+1
for i in gen():
    print(i)
    

import re


file = open("a.txt", "r")
data = file.read()

x = "[ab]"
r = "[ba]"
a = re.sub(x, r, data)
print(data)

'''
a =  "abcsajcdksjыофавы"
c = 0
for i in a:
    if not i.isspace():
        c = c+1
print(c)
'''