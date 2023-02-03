n_broi = int(input())
b_broi = int(input())
r_broi = int(input())
m_chasove = int(input())
n_cena = (n_broi + 2) * 1.5
b_cena = (b_broi + ((b_broi * 10) / 100)) * 14.5
r_cena = r_broi * 5
t_cena = 0.4
m_cena = (((n_cena + b_cena + r_cena + t_cena) * 30) / 100) * m_chasove
print(n_cena + b_cena + r_cena + t_cena + m_cena)