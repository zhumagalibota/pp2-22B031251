#code 1
thislist = ["apple", "banana", "cherry"]
print(thislist)

#code 2
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#code 3
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#code 4
list1 = ["abc", 34, True, 40, "male"]

#code 5
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#code 5
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#access list items code 1
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#code 2
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#code 3
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#code 4
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

#code 5
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#code 6
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#code 7
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#add ist items code 1
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#code 2
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#code 3
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#code 4
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#remove list items code 1
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#code 2
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#code 3
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#code 4
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#code 5
thislist = ["apple", "banana", "cherry"]
del thislist

#code 6
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#loop lists code 1
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#code 2
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#code 3
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#code 4
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#list comprehension code 1
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)

#code 2
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

#code 3
newlist = [x for x in fruits if x != "apple"]

#code 4
newlist = [x for x in fruits]

#code 5
newlist = [x for x in range(10)]

#code 6
newlist = [x for x in range(10) if x < 5]

#code 7
newlist = [x.upper() for x in fruits]

#code 8
newlist = ['hello' for x in fruits]

#code 9
newlist = [x if x != "banana" else "orange" for x in fruits]

