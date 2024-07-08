# element-wise 방식으로 같으면 0, 다르면 1

# row 개수 n, column 개수 m
n, m = map(int, input().split())

# 각 배열 선언
arr_1 = [
    list(map(int, input().split()))
    for _ in range(n)
]
arr_2 = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 리스트 컴프리헨션으로 result_arr 생성
result_arr = [
    [
        0 if arr_1[i][j] == arr_2[i][j] else 1
        for j in range (m)
    ]
    for i in range(n)
]

for row in result_arr:
    for element in row:
        print(element, end=" ")
    print()