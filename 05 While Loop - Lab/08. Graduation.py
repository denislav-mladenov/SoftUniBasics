name = input()
grades_total = 0
years = 0
failed = 0

while True:
    annual_grades = float(input())
    years += 1

    if annual_grades < 4:
        failed += 1
        if failed == 2:
            print(f"{name} has been excluded at {years} grade")
            break
        years -= 1
    else:
        grades_total += annual_grades

    if years == 12:
        average = grades_total / 12
        print(f"{name} graduated. Average grade: {average:.2f}")
        break