arr = [
    [0 for _ in range(5)]
    for _ in range(5)
]

# 첫 번째 행을 1로 채움
for j in range(5):
    arr[0][j] = 1

# 첫 번째 열을 1로 채움
for i in range(5):
    arr[i][0] = 1

for row in range(1,5):
    for col in range(1,5):
        # [현재 행, 현재 열] = [현재 행 -1][현재 열] + [현재 행][현재 열 -1]
        arr[row][col] = arr[row-1][col] + arr[row][col-1] 

for row in arr:
    print(*row)