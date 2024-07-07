n = 5

# list comprehension을 통한 리스트 선언
arr_2d =[
    list(input().split())
    for _ in range(n)
]

# 2중 for문 사용
for i in range(n):
    for j in range(len(arr_2d[i])):
        print(arr_2d[i][j].upper(), end = " ")
    print()