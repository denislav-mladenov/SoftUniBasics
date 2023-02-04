import math

s1 = int(input())
s2 = int(input())
s3 = int(input())
time = s1 + s2 + s3
minutes = time / 60
seconds = time % 60
minutes = math.floor(minutes)
if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')