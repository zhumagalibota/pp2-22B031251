import re
import codecs


file = codecs.open( "row.txt", "r", "utf-8" )
data = file.read()

#1
x = re.findall("[а-яА-Я]*аб*[а-я]*", data)
print(x)

#2----------------
x = re.search("[а-яА-Я]*аб{2,3}[а-я]*", data)
print(x)
#3---------------      
x = re.search("[а-я]*_[а-я]*", data)
print(x)

#4
x = re.findall("[А-Я][а-я]+", data)
print(x)

