arr = list(map(int, input().split()))

even_arr = arr[1:len(arr)+1:2]
sum_even = sum(even_arr)

third_arr = arr[2:len(arr)+1:3]
sum_third = sum(third_arr)
avg_third = round(sum_third / len(third_arr), 2)

print(f'{sum_even} {avg_third}')