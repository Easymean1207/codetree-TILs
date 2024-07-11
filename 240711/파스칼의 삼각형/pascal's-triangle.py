n = int(input())

arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

# 첫 항은 모두 0
for i in range(n):
    for j in range(n):
        arr[i][0] = 1

# 파스칼의 삼각형 법칙 적용: arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
for i in range(1, n):
    for j in range(1, n):
        arr[i][j] = arr[i-1][j-1]+arr[i-1][j]

for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            print(arr[i][j], end = ' ')
    print()