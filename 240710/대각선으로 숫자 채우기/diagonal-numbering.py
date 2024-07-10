# n = row, m = column
n, m = map(int, input().split())

arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]

''' 핵심 로직: 대각선의 합은 같음. '''
# 최대 대각선 합, 초기 값 선언
max_cnt = (n-1)+ (m-1)
value = 1

for current_cnt in range(max_cnt+1):
    for row in range(n):
        for column in range(m):
            if current_cnt == row + column:
                arr[row][column] = value
                value+=1


for row in arr:
    print(*row)