n = int(input())

arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

# 첫 번째 행, 열 1로 초기화
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0:
            arr[i][j] = 1

for i in range(1, n):
    for j in range(1, n):
        arr[i][j] = arr[i-1][j-1] + arr[i-1][j] + arr[i][j-1]

for row in arr:
    print(*row)