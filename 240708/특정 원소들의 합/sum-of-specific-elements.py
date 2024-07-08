# 2차원 배열 선언
arr_2d = [
    list(map(int, input().split()))
    for _ in range(4)
]

result = 0

for i in range(4):
    for j in range(i+1):
        result += arr_2d[i][j]

print(result)