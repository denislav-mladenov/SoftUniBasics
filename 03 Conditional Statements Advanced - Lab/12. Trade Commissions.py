city = input()
money = float(input())
bonus = 0

if city in ["Sofia", "Varna", "Plovdiv"]:
    if 0 <= money <= 500:
        if city == "Sofia":
            bonus = money * 0.05
            print(f"{bonus:.2f}")
        elif city == "Varna":
            bonus = money * 0.045
            print(f"{bonus:.2f}")
        elif city == "Plovdiv":
            bonus = money * 0.055
            print(f"{bonus:.2f}")
    elif 501 <= money <= 1000:
        if city == "Sofia":
            bonus = money * 0.07
            print(f"{bonus:.2f}")
        elif city == "Varna":
            bonus = money * 0.075
            print(f"{bonus:.2f}")
        elif city == "Plovdiv":
            bonus = money * 0.08
            print(f"{bonus:.2f}")
    elif 1001 <= money <= 10000:
        if city == "Sofia":
            bonus = money * 0.08
            print(f"{bonus:.2f}")
        elif city == "Varna":
            bonus = money * 0.1
            print(f"{bonus:.2f}")
        elif city == "Plovdiv":
            bonus = money * 0.12
            print(f"{bonus:.2f}")
    elif money > 10000:
        if city == "Sofia":
            bonus = money * 0.12
            print(f"{bonus:.2f}")
        elif city == "Varna":
            bonus = money * 0.13
            print(f"{bonus:.2f}")
        elif city == "Plovdiv":
            bonus = money * 0.145
            print(f"{bonus:.2f}")
    else:
        print("error")
else:
    print("error")