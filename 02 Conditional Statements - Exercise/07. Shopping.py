budget = float(input())
video_cards_count = int(input())
processor_count = int(input())
ram_count = int(input())

cash_video = video_cards_count * 250
cash_processor = (cash_video * 0.35) * processor_count
cash_ram = (cash_video * 0.1) * ram_count
total_price = cash_video + cash_processor + cash_ram

if video_cards_count >= processor_count:
    total_price -= (total_price * 0.15)

if budget >= total_price:
    total_price_left = budget - total_price
    print(f"You have {total_price_left:.2f} leva left!")
else:
    diff = (abs(budget - total_price))
    print(f"Not enough money! You need {diff:.2f} leva more!")