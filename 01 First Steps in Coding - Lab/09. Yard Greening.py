yards = float(input())
price_kv = yards * 7.61
discount = price_kv * 0.18
total = price_kv - discount

print(f"The final price is: {total} lv.")
print(f"The discount is: {discount} lv.")