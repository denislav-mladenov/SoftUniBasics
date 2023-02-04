fruit = input()
day_of_week = input()
pieces = float(input())
price = 0
if fruit in ["banana", "apple", "orange", "grapefruit", "kiwi", "pineapple", "grapes"]:
    if day_of_week in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
        if fruit == "banana":
            price = pieces * 2.5
            print(f"{price:.2f}")
        elif fruit == "apple":
            price = pieces * 1.2
            print(f"{price:.2f}")
        elif fruit == "orange":
            price = pieces * 0.85
            print(f"{price:.2f}")
        elif fruit == "grapefruit":
            price = pieces * 1.45
            print(f"{price:.2f}")
        elif fruit == "kiwi":
            price = pieces * 2.7
            print(f"{price:.2f}")
        elif fruit == "pineapple":
            price = pieces * 5.5
            print(f"{price:.2f}")
        elif fruit == "grapes":
            price = pieces * 3.85
            print(f"{price:.2f}")
    elif day_of_week in ["Saturday", "Sunday"]:
        if fruit == "banana":
            price = pieces * 2.7
            print(f"{price:.2f}")
        elif fruit == "apple":
            price = pieces * 1.25
            print(f"{price:.2f}")
        elif fruit == "orange":
            price = pieces * 0.9
            print(f"{price:.2f}")
        elif fruit == "grapefruit":
            price = pieces * 1.6
            print(f"{price:.2f}")
        elif fruit == "kiwi":
            price = pieces * 3
            print(f"{price:.2f}")
        elif fruit == "pineapple":
            price = pieces * 5.6
            print(f"{price:.2f}")
        elif fruit == "grapes":
            price = pieces * 4.2
            print(f"{price:.2f}")
    else:
        print("error")
else:
    print("error")