n = int(input())

# 배열 선언
arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for i in range(n):
    for j in range(n):
        # 각 값은 등차수열 방식으로 채워짐.
        arr[i][j] = n * j + (i+1)

for row in arr:
    ''' unpacking을 이용하지 않는 방식 '''
    # for elem in row:
    #     print(elem, end = " ")
    # print()

    ''' unpacking을 이용한 방식 '''
    print(*row)