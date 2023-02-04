import sys

count_numbers = int(input())
max_number = -sys.maxsize
suma = 0

for i in range(1, count_numbers + 1):
    new_number = int(input())
    if new_number > max_number:
        max_number = new_number
    suma += new_number

total = suma - max_number
if total == max_number:
    print("Yes")
    print(f"Sum = {total}")
else:
    diff = abs(total - max_number)
    print("No")
    print(f"Diff = {diff}")