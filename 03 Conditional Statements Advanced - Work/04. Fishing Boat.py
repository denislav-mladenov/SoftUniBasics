budget = int(input())
season = input()
members = int(input())

boat_price = 0

if season == "Spring":
    boat_price = 3000
elif season == "Summer" or season == "Autumn":
    boat_price = 4200
elif season == "Winter":
    boat_price = 2600

if members <= 6 and members != 0:
    boat_price = boat_price * 0.9
elif 7 <= members <= 11:
    boat_price = boat_price * 0.85
elif members > 11:
    boat_price = boat_price * 0.75

if members % 2 == 0 and season != "Autumn":
    boat_price = boat_price * 0.95

diff = abs(boat_price - budget)
if budget >= boat_price:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")

