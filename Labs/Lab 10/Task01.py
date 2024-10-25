from random import randint

length = 12
x = [randint(10, 99) for _ in range(length)]
print('Monthly Sales:', ' '.join(map(str, x)))

quarters = [(0, 3),(3, 6),(6, 9),(9, 12)]

for q, (start, end) in enumerate(quarters, start=1):
    quarter_sales = x[start:end]
    min_sale = min(quarter_sales)
    max_sale = max(quarter_sales)
    avg_sale = sum(quarter_sales) / len(quarter_sales)
    
    print(f"Quarter {q}: {' '.join(map(str, quarter_sales))}")
    print(f"Min = {min_sale}, Max = {max_sale}, Average = {avg_sale:.2f}")
    print()
