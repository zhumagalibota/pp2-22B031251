#code 1
mytuple = ("apple", "banana", "cherry")

#code 2
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#code 3
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#code 4
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#code 5
thistuple = ("apple",)
print(type(thistuple))

#code 6
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

#code 7
tuple1 = ("abc", 34, True, 40, "male")
type()

#code 8
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

#code 9
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

#access tuples code 1
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#code 2
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

#code 3
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

#code 4
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

#code 5
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

#code 6
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

#code 7
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

#update tuples code 1
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

#code 2
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

#code 3
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

#code 4
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

#code 5
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

#unpack tuple code 1
fruits = ("apple", "banana", "cherry")

#code 2
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

#code 3
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

#code 4
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)

#loop tuple code 1
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#code 2
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

#code 3
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

#join tuple code 1
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

#code 2
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)