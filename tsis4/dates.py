import datetime

#1
x = datetime.datetime.now()
a = x.strftime("%d")
b = int(a) - 5
print("Current date:", a, "\nsubtracted five days:", b)
