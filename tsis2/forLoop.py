#code 1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#code 2
for x in "banana":
  print(x)

#code 3
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#code 4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

#code 5
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#code 6
for x in range(6):
  print(x)

#code 7
for x in range(2, 6):
  print(x)

#code 8
for x in range(2, 30, 3):
  print(x)

#code 9
for x in range(6):
  print(x)
else:
  print("Finally finished!")

#code 10
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

#code 11
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)

#code 12
for x in [0, 1, 2]:
  pass
