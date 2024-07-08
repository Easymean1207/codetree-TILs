# 각 배열 선언
arr_1st = [
    list(map(int, input().split()))
    for _ in range(3)
]

# 입력 줄 바꿈 제거
input()

arr_2nd = [
    list(map(int, input().split()))
    for _ in range(3)
]

arr_mul = [
    [0 for _ in range(len(arr_1st[0]))]
    for _ in range(3)
]

for i in range(3):
    for j in range(len(arr_1st[0])):
        arr_mul[i][j] = arr_1st[i][j] * arr_2nd[i][j]
    
for each_row in arr_mul:
    print(*each_row)