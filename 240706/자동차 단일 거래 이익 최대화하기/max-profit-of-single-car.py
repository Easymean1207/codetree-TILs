import sys

n_year = int(input())
price_of_each_year = list(map(int, input().split()))

# 초기 최소 가격과 최대 이익 초기화
min_price = sys.maxsize
max_profit = 0

for price in price_of_each_year:
    # 현재 가격이 최소 가격보다 작으면 최소 가격 갱신
    if price < min_price:
        min_price = price
        
    # 현재 가격과 최소 가격의 차이를 계산하여 최대 이익 갱신
    elif price - min_price > max_profit:
        max_profit = price - min_price

print(max_profit)