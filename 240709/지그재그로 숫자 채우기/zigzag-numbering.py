# n = row 개수, m = column 개수
n, m = map(int, input().split())

arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]

# 홀수 번째 원소들과 짝수 번째 원소들은 각각 등차수열
for i in range(n):
    for j in range(m):
        # 홀수 번째 원소의 경우 (j=0,2,4,6....)
        if j % 2 == 0:
            arr[i][j] = (n*2)*(j//2)+i
        # 짝수 번째 원소의 경우(j=1,3,5,7...)
        else:
            arr[i][j] = (n*2)*((j-1)//2) + (2*n-1-i)

for i in range(n):
    for j in range(m):
        print(arr[i][j], end = ' ')
    print()