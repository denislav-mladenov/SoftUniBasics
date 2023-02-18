judges = int(input())
presentation = input()

all_grades = 0
count_grades = 0

while presentation != "Finish":
    total = 0
    for i in range(1, judges + 1):
        grade = float(input())
        total += grade
        all_grades += grade
        count_grades += 1
    average = total / judges
    print(f"{presentation} - {average:.2f}.")

    presentation = input()
very_final = all_grades / count_grades
print(f"Student's final assessment is {very_final:.2f}." )

