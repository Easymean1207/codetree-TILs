n_cnt = int(input())

result = 0

for _ in range(n_cnt):
    num = int(input())
    result+=num

result = str(result)
left_shifted = result[1:] + result[0]

print(left_shifted)