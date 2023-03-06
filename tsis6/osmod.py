import os
'''
#1
path = '/'
a = os.listdir(path)
print(a)

#2
path = '/Python311'
a = os.access(path, os.F_OK)
print(a)
if a:
    b = os.access(path, os.R_OK)
    print(b)
    c = os.access(path, os.W_OK)
    print(c)
    d = os.access(path, os.X_OK)
    print(d)

#3
path = '/Python311'
a = os.path.exists(path)
if a:
    print(
    "file name:", os.path.basename(path), 
    "\ndirectory:", os.path.dirname(path)
    )
else:
    print("path does not exist")

#4
a = open(r'osmod.py', 'r')
count, count1 = 0, 0
for i in a:
    if i != '\n':
        count += 1
    else:
        count1 += 1
    print(count+count1)

#5
a = open('b.txt', 'w')
b = ["1", "2", "3"]
for i in b:
    a.write(i+' ')
a.close()
a = open('b.txt', 'r')
print(a.read())

#6
import string

a = string.ascii_uppercase[:26]
for i in a:
    b = i+".txt"
   #f = open(b, 'w')
   #os.remove(b)'''

#7----------------------

#8
path = "a.py"
a = os.access(path, os.F_OK)
if a:
    os.remove(path)
else:
    print("file does not exist")

