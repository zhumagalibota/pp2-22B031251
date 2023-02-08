#1
def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    print(ounces)

#grams = int(input())
#grams_to_ounces(grams)

#2
def temperature_conversion(F):
    C = (5 / 9) * (F - 32)
    print(C)

#F = int(input())
#temperature_conversion(F)

#3
def solve(numheads, numlegs):
    chickens = (numheads * 4 - 94) / 2
    rabbits = numheads - chickens
    print('chickens:', chickens, 'rabbits:', rabbits)

#solve(35, 94)




#9
def volume_of_sphere(r):
    volume = (4 * 3.14 * r**3) / 3
    print(round(volume, 3))
#r = int(input())
#volume_of_sphere(r)


#11
def palindrome(p):
    i = p.replace(" ", "")
    reverse = i[::-1]
    if reverse == i:
        print('yes')
    else:
        print('no')
#p = input()
#palindrome(p)

#12
def histogram(l):
    for i in range(0, len(l)):
        k = int(l[i])
        j = '*' * k
        print(j)      
#l = input().split()
#histogram(l)

#13
import random
def random_number_game():
    count = 0
    b = random.randint(1, 20)
    while b > 0:
        a = int(input())
        if a < b:
            print("Your guess is too low.\nTake a guess.")
            count = count + 1    
        elif a > b:
            print("Your guess is too high.\nTake a guess.")
            count = count + 1
        else:
            print("Good job, ", name, "! You guessed my number in ", count, " guesses!", sep='')
            break
  
'''print("Hello! What is your name?")
name = input()
print("Well, ", name, ", I am thinking of a number between 1 and 20.\n", 'Take a guess.', sep="")
random_number_game()'''




