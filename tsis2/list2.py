
#sort list code 1
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#code 2
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#code 3
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#code 4
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#code 5
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#code 6
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

#code 7
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#code 8
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

#copy list code 1
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#code 2
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#join list code 1
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

#code 2
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)

#code 3
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)