#1
'''n = int(input())
a = (x**2 for x in range(1, n))
for x in a:
    print(x)
    if x >= n:
        break

#2
n = int(input())
def gen(n):
    for v in range(n):
        if v%2==0:
            yield v
            v += 1          
l = list(gen(n))
print(*gen(n+1), sep=", ")

#3
def gen(n):
    for v in range(n):
        if v%3==0 and v%4==0:
            yield v
            v += 1
for v in gen(100):
    print(v)

#4
a = int(input())
b = int(input())
a = (v**2 for v in range(a, b))
for v in a:
    print(v)'''

#5
def gen(v):
    while v>=0:
        yield v
        v = v-1
for i in gen(10):
    print(i)




    