pile_menu = 10.35
riba_menu = 12.40
vege_menu = 8.15
dostavka = 2.5
pile_broi = int(input())
riba_broi = int(input())
vege_broi = int(input())
poruchka = pile_broi * pile_menu + riba_broi * riba_menu + vege_broi * vege_menu
desert = (poruchka * 20) / 100
total = poruchka + desert + 2.5
print(total)