sofia_coffee = 0.5
sofia_water = 0.8
sofia_beer = 1.2
sofia_sweets = 1.45
sofia_peanuts = 1.6

plovdiv_coffee = 0.4
plovdiv_water = 0.7
plovdiv_beer = 1.15
plovdiv_sweets = 1.3
plovdiv_peanuts = 1.5

varna_coffee = 0.45
varna_water = 0.7
varna_beer = 1.1
varna_sweets = 1.35
varna_peanuts = 1.55

product = input()
city = input()
pieces = float(input())

if city == "Sofia":
    if product == "coffee":
        price = pieces * sofia_coffee
        print(price)
    elif product == "water":
        price = pieces * sofia_water
        print(price)
    elif product == "beer":
        price = pieces * sofia_beer
        print(price)
    elif product == "sweets":
        price = pieces * sofia_sweets
        print(price)
    elif product == "peanuts":
        price = pieces * sofia_peanuts
        print(price)
if city == "Plovdiv":
    if product == "coffee":
        price = pieces * plovdiv_coffee
        print(price)
    elif product == "water":
        price = pieces * plovdiv_water
        print(price)
    elif product == "beer":
        price = pieces * plovdiv_beer
        print(price)
    elif product == "sweets":
        price = pieces * plovdiv_sweets
        print(price)
    elif product == "peanuts":
        price = pieces * plovdiv_peanuts
        print(price)
if city == "Varna":
    if product == "coffee":
        price = pieces * varna_coffee
        print(price)
    elif product == "water":
        price = pieces * varna_water
        print(price)
    elif product == "beer":
        price = pieces * varna_beer
        print(price)
    elif product == "sweets":
        price = pieces * varna_sweets
        print(price)
    elif product == "peanuts":
        price = pieces * varna_peanuts
        print(price)
