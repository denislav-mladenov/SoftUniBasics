pens = int(input())
markers = int(input())
preparats = int(input())
percent = int(input())
pens_price = pens * 5.8
markers_price = markers * 7.2
preparats_price = preparats * 1.2
total = (pens_price + markers_price + preparats_price)
final = total - ((total * percent) / 100)
print(final)