daljina = int(input())
shirina = int(input())
visochina = int(input())
procent = float(input())
obem_akva = daljina * shirina * visochina
obem_litri = obem_akva / 1000
total = obem_litri * (1 - (procent / 100))
print(total)