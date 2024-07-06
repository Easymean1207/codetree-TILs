n_year = int(input())
price_of_each_year = list(map(int, input().split()))

# 최소 가격과 인덱스 지정
min_price = min(price_of_each_year)
min_idx = price_of_each_year.index(min_price)

# 최소 인덱스 ~ 끝 중 가장 큰 값을 확인
max_price = max(price_of_each_year[min_idx:])
max_idx = price_of_each_year.index(max_price)

# 이익: -(min_price - max_price)
profit = -(min_price - max_price)

if profit > 0:
    print(profit)
else:
    profit = 0
    print(profit)