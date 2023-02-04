tabs = int(input())
salary = int(input())
salary_left = salary

for t in range(1, tabs + 1):
    one_tab = input()
    if one_tab == "Facebook":
        salary_left -= 150
    elif one_tab == "Instagram":
        salary_left -= 100
    elif one_tab == "Reddit":
        salary_left -= 50

    if salary_left <= 0:
        break

if salary_left <= 0:
    print("You have lost your salary.")
else:
    print(salary_left)