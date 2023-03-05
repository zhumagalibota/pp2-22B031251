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

#5
x = re.search("\Aа[а-я1-9]*б", data)
print(x)

#6
a = "[\s|,|.]+"
r = ":"
x = re.sub(a, r, data)
print(x)

#7
x = re.sub('-+[а-я]', r, data)


#8
x = re.sub(r'([А-Я])', r'\1,', data)
print(x)

#9
x = re.sub(r'([А-Я][а-яА-Я]+)', r' \1', data)
print(x)