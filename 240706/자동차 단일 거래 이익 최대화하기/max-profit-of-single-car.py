import sys

n_year = int(input())
price_of_each_year = list(map(int, input().split()))

min_price = sys.maxsize
profit = 0

for price in price_of_each_year:

    if price < min_price:
        min_price = price
    elif price - min_price > profit:
        profit = price - min_price

print(profit)