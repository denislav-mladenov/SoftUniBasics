import math

name_serial = input()
episod_duration = int(input())
relax_duration = int(input())

lunch = relax_duration * 0.125
rest = relax_duration * 0.25
time_needed = lunch + rest + episod_duration

diff = math.ceil(abs(relax_duration - time_needed))

if time_needed <= relax_duration:
    print(f"You have enough time to watch {name_serial} and left with {diff} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_serial}, you need {diff} more minutes.")