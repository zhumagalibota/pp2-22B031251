import re
import codecs


file = codecs.open( "row.txt", "r", "utf-8" )
data = file.read()

#1
x = re.search("[a-zA-Z]*a(b*)[a-zA-Z]*", data)
print(x)

#2
x = re.search("[a-zA-Z]*a(b{2|3})[a-zA-Z]*", data)
print(x)