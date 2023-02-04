name_actor = input()
points_academy = float(input())
judges = int(input())

final_points = points_academy

for o in range(1, judges + 1):
    name_judge = input()
    points_from_judges = float(input())

    final_points = final_points + ((len(name_judge) * points_from_judges) / 2)

    if final_points >= 1250.5:
        break

if final_points < 1250.5:
    diff = abs(final_points - 1250.5)
    print(f"Sorry, {name_actor} you need {diff:.1f} more!")
else:
    print(f"Congratulations, {name_actor} got a nominee for leading role with {final_points:.1f}!")
