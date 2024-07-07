n = 2

# 2차원 배열 선언
arr_2d = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 가로 합과 세로 합(list), 전체 합(int)을 저장할 자료형 선언
row_sums = [0 for _ in range(n)]
column_sums = [0 for _ in range(len(arr_2d[0]))]
all_sum = 0

for i in range(n):
    # 각 행마다 해당 가로합 갱신
    row_sums[i] += sum(arr_2d[i])

    # 각 열에 맞게 해당 세로합 갱신
    for j in range(len(arr_2d[i])):
        column_sums[j] += arr_2d[i][j]
        all_sum += arr_2d[i][j]

# row_avg == row_sum / 열의 길이(len(arr_2d[0]))
# column_avg == column_sum / 행의 길이(n)
# all_avg == all_sum / 전체 개수 (행 x 열)
row_avg = [row_sum/len(arr_2d[0]) for row_sum in row_sums]
column_avg = [column_sum/n for column_sum in column_sums]
all_avg = all_sum / (n * len(arr_2d[0]))

print(*row_avg)
print(*column_avg)
print(all_avg)