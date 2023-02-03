taksa = int(input())
kecove = taksa - (taksa * 40) / 100
ekip = kecove - (kecove * 20) / 100
topka = ekip * 0.25
aksesoari = topka * 0.2
total = taksa + kecove + ekip + topka + aksesoari
print(total)