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

''' for문을 이용한 방식 '''
# arr_mul(element-wise 방식의 곱이 들어간 배열)
# arr_mul = [
#     [0 for _ in range(len(arr_1st[0]))]
#     for _ in range(3)
# ]

# for i in range(3):
#     for j in range(len(arr_1st[0])):
#         arr_mul[i][j] = arr_1st[i][j] * arr_2nd[i][j]
    
''' 리스트 컴프리헨션을 이용한 방식 '''
arr_mul = [
    [arr_1st[i][j] * arr_2nd[i][j] for j in range(len(arr_1st[0]))]
    for i in range(3)
]

for each_row in arr_mul:
    print(*each_row)