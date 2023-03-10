first_num = int(input())
second_num = int(input())
operator = input()

result = 0
if operator == "+":
    result = first_num + second_num
    if result % 2 == 0:
        print(f"{first_num} + {second_num} = {result} - even")
    else:
        print(f"{first_num} + {second_num} = {result} - odd")
elif operator == "-":
    result = first_num - second_num
    if result % 2 == 0:
        print(f"{first_num} - {second_num} = {result} - even")
    else:
        print(f"{first_num} - {second_num} = {result} - odd")
elif operator == "*":
    result = first_num * second_num
    if result % 2 == 0:
        print(f"{first_num} * {second_num} = {result} - even")
    else:
        print(f"{first_num} * {second_num} = {result} - odd")
elif operator == "/" and second_num != 0:
    result = first_num / second_num
    print(f"{first_num} / {second_num} = {result:.2f}")
elif operator == "%" and second_num != 0:
    result = first_num % second_num
    print(f"{first_num} % {second_num} = {result}")

if second_num == 0 and (operator == "/" or operator == "%"):
    print(f"Cannot divide {first_num} by zero")