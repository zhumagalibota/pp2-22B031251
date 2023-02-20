import datetime

#1
x = datetime.datetime.now()
a = datetime.timedelta(5)
b = x - a
print("Current date:", x, "\nsubtracted five days:", b)
'''
#2
today = datetime.datetime.now() 
x = datetime.timedelta(1)
yesterday = today - x
tomorrow = today + x
print("Today:", today.strftime("%A"), 
      "\nYesterday:", yesterday.strftime("%A"),
      "\nTomorrow:", tomorrow.strftime("%A"))

#3
x = datetime.datetime.now()
a = datetime.datetime.now().replace(microsecond = 0)
print("With:", x, "\nWithout:", a)

#4
a = datetime.date(2012, 4, 8)
b = datetime.date(2021, 6, 7)
c = b - a
print(c.total_seconds())'''