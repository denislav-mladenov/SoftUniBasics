budget = float(input())
statisti = int(input())
cena_obleklo = float(input())

dekor = budget - ((budget * 10) / 100)
dekor = budget - dekor

if statisti > 150:
    cena_obleklo = cena_obleklo - ((cena_obleklo * 10) / 100)

cena_obleklo = cena_obleklo * statisti
suma_film = cena_obleklo + dekor

diff = abs(budget - suma_film)
if budget >= suma_film:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")