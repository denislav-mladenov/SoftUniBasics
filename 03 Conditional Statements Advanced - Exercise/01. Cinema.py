type_movie = input()
count_r = int(input())
count_c = int(input())

if type_movie == "Premiere":
    total = count_r * count_c
    total = total * 12
    print(f"{total:.2f} leva")
elif type_movie == "Normal":
    total = count_r * count_c
    total = total * 7.5
    print(f"{total:.2f} leva")
elif type_movie == "Discount":
    total = count_r * count_c
    total = total * 5
    print(f"{total:.2f} leva")