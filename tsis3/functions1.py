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

solve(35, 94)
