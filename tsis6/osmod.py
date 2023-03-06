import os
'''
#1
path = '/'
a = os.listdir(path)
print(a)
'''
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
'''
path = '/Python311'
a = os.path.exists(path)
if a:
    print(
    "file name:", os.path.basename(path), 
    "\ndirectory:", os.path.dirname(path)
    )
else:
    print("path does not exist")'''
