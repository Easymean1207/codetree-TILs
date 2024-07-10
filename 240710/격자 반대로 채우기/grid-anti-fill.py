n = int(input())

# 격자 선언
mat = [
    [0 for _ in range(n)]
    for _ in range(n)
]

# 초기값 선언
value = 1

for col in range(n-1, -1, -1):
    # n이 짝수일 때
    if n % 2 == 0:
        # col 값이 짝수인 경우 -> 정방향
        if col % 2 == 0:
            for row in range(n):
                mat[row][col] = value
                value += 1

        # col 값이 홀수인 경우 -> 역방향
        else:
            for row in range(n - 1, -1, -1):
                mat[row][col] = value
                value += 1
    
    # n이 홀수 일때
    else:
        # col 값이 홀수인 경우 -> 정방향
        if col % 2 != 0:
            for row in range(n):
                mat[row][col] = value
                value += 1

        # col 값이 짝수인 경우 -> 역방향
        else:
            for row in range(n - 1, -1, -1):
                mat[row][col] = value
                value += 1


for row in range(n):
    for column in range(n):
        print(mat[row][column], end = ' ')
    print()