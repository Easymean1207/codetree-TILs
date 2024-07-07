n = 5
arr_2d =[
    list(input().split())
    for _ in range(n)
]

for i in range(n):
    for j in range(len(arr_2d[i])):
        print(arr_2d[i][j].upper(), end = " ")
    print()