#1
'''n = int(input())
a = (x**2 for x in range(1, n))
for x in a:
    print(x)
    if x >= n:
        break'''

#2
n = int(input())
even = (x%2 for x in range(1, n))
for x in even:
    print(x)
    if x >= n:
        break