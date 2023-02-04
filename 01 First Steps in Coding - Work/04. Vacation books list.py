count_pages = int(input())
pages_per_hour = int(input())
days_for_book = int(input())
hours = count_pages / pages_per_hour
hours_day = hours / days_for_book
print(int(hours_day))