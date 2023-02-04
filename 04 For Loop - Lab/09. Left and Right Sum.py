numbers = int(input())
suma = 0
suma2 = 0
for i in range(numbers):
    new_number = int(input())
    suma += new_number

for i in range(numbers):
    new_number1 = int(input())
    suma2 += new_number1

diff = abs(suma - suma2)

if suma == suma2:
    print(f"Yes, sum = {suma}")
if suma != suma2:
    print(f"No, diff = {diff}")