#code 1
thisset = {"apple", "banana", "cherry"}
print(thisset)

#code 2
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

#code 3
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

#code 4
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

#code 5
set1 = {"abc", 34, True, 40, "male"}
type()

#code 6
myset = {"apple", "banana", "cherry"}
print(type(myset))

#code 7
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

#access set code 1
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

#code 2
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

#add set code 1
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

#code 2
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

#code 3
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

#remove set items code 1
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

#code 2
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

#code 3
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

#code 4
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

#code 5
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)

#loop code 1
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

#join code 1
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

#code 2
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

#code 3
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

#code 4
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)

#code 5
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

#code 6
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)

