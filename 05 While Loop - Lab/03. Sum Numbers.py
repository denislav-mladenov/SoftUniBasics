max_num = int(input())
suma = 0

while suma <= max_num:
    new_num = int(input())
    suma += new_num
    if suma >= max_num:
        print(suma)
        break