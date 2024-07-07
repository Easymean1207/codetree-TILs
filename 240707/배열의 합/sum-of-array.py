n = 4

# # 2차원 배열 생성 (append를 이용한 방법)
# arr_2d = []
# for _ in range(n):
#     arr = list(map(int, input().split()))
#     arr_2d.append(arr)

# 2차원 배열 생성 (list comprehension 방법)
arr_2d = [
    list(map(int, input().split()))
    for _ in range(n)
]

for i, item in enumerate(arr_2d):
    each_sum = sum(arr_2d[i])
    print(each_sum)