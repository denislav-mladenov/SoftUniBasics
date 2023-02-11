max_num = -1000000000

while True:
    current_num = input()

    if current_num == 'Stop':
         break

    current_num = int(current_num)
    if current_num >= max_num:
        max_num = current_num
    else:
        pass



print(max_num)