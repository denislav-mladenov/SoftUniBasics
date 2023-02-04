tournaments = int(input())
start_points = int(input())
all_points = start_points
w = 2000
f = 1200
sf = 720
win_tour = 0
for t in range(1, tournaments + 1):
    positions = input()

    if positions == "W":
        all_points += w
        win_tour += 1
    if positions == "F":
        all_points += f
    if positions == "SF":
        all_points += sf
print(f"Final points: {all_points}")
average = int((all_points - start_points) / tournaments)
print(f"Average points: {average}")
percent_wins = (win_tour / tournaments) * 100
print(f"{percent_wins:.2f}%")

