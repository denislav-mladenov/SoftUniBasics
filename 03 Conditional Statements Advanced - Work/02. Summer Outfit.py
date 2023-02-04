degree = int(input())
time = input()

if 10 <= degree <= 18:
    if time == "Morning":
        Outfit = "Sweatshirt"
        Shoes = "Sneakers"
        print(f"It's {degree} degrees, get your {Outfit} and {Shoes}.")
    elif time == "Afternoon":
        Outfit = "Shirt"
        Shoes = "Moccasins"
        print(f"It's {degree} degrees, get your {Outfit} and {Shoes}.")
    elif time == "Evening":
        Outfit = "Shirt"
        Shoes = "Moccasins"
        print(f"It's {degree} degrees, get your {Outfit} and {Shoes}.")
elif 18 < degree <= 24:
    if time == "Morning":
        Outfit = "Shirt"
        Shoes = "Moccasins"
        print(f"It's {degree} degrees, get your {Outfit} and {Shoes}.")
    elif time == "Afternoon":
        Outfit = "T-Shirt"
        Shoes = "Sandals"
        print(f"It's {degree} degrees, get your {Outfit} and {Shoes}.")
    elif time == "Evening":
        Outfit = "Shirt"
        Shoes = "Moccasins"
        print(f"It's {degree} degrees, get your {Outfit} and {Shoes}.")
elif degree >= 25:
    if time == "Morning":
        Outfit = "T-Shirt"
        Shoes = "Sandals"
        print(f"It's {degree} degrees, get your {Outfit} and {Shoes}.")
    elif time == "Afternoon":
        Outfit = "Swim Suit"
        Shoes = "Barefoot"
        print(f"It's {degree} degrees, get your {Outfit} and {Shoes}.")
    elif time == "Evening":
        Outfit = "Shirt"
        Shoes = "Moccasins"
        print(f"It's {degree} degrees, get your {Outfit} and {Shoes}.")