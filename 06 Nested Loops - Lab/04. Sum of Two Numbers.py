start = int(input())
final = int(input())
number = int(input())

counter = 0
flag = False

for a in range(start, final + 1):
    for b in range(start, final + 1):
        counter += 1

        if a + b == number:
            print(f"Combination N:{counter} ({a} + {b} = {number})")
            flag = True
            break
    if flag:
        break

if not flag:
    print(f"{counter} combinations - neither equals {number}")