import math

record_seconds = float(input())
razstoqnie_metri = float(input())
seconds_for_1_m = float(input())

all_time = razstoqnie_metri * seconds_for_1_m
total_time_delay = math.floor(razstoqnie_metri / 15) * 12.5
all_time_final = all_time + total_time_delay


if record_seconds <= all_time_final:
    diff = (all_time_final - record_seconds)
    print(f"No, he failed! He was {diff:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {all_time_final:.2f} seconds.")