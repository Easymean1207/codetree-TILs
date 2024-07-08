# 가로변의 길이 m -> column 개수
# 세로변의 길이 n -> row 개수
n, m = map(int, input().split())

arr_2d = [
    [0 for _ in range(m)]
    for _ in range(n)
]


# arr[0][0]의 값 설정
value = 1

for row in range(n):
    for column in range(m):
        arr_2d[row][column] = value
        value+=1

for each_row in arr_2d:
    print(*each_row)