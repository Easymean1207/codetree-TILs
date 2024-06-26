ls = list(map(int,input().split()))

odd_ls = ls[::2]
even_ls = ls[1::2]

sum_odd = sum(odd_ls)
sum_even = sum(even_ls)

diff = abs(sum_odd - sum_even)

print(diff)