points = int(input())
points_total = 0


if points <= 100:
    points_total = points + 5
elif points > 1000:
    points_total = points + ((points * 10) / 100)
else:
    points_total = points + ((points * 20) / 100)

if points % 2 == 0:
    points_total = points_total + 1
elif points % 10 == 5:
    points_total = points_total + 2

points_bonus = points_total - points

print(points_bonus)
print(points_total)