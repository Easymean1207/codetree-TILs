import sys

n_year = int(input())
price_of_each_year = list(map(int, input().split()))

min_price = price_of_each_year[0]
max_profit = 0

# 핵심 아이디어: 사는 시기가 아닌 파는 시기를 기준으로 생각
# 파는 시기에서 가장 최소가 되는 인덱스의 값을 빼면 그것이 최대 이익
for i, price in enumerate(price_of_each_year):
    # 현재 가격에서 이익 계산
    profit = price - min_price

    if profit > max_profit:
        max_profit = profit
    
    if price < min_price:
        min_price = price

print(max_profit)