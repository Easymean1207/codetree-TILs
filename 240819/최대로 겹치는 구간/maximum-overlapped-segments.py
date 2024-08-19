OFFSET = 100
MAX_RANGE = 200

# 입력 구간 n개
n = int(input())
# 각 구간
segments = [
    tuple(map(int, input().split()))
    for _ in range(n)
]
common = [0 for _ in range (MAX_RANGE+1)]

for x1, x2 in segments:
    x1, x2 = x1 + OFFSET, x2 + OFFSET

    # 구간의 경우 시작점만을 count하므로 등호가 들어가지 않음.
    for i in range(x1, x2):
        common[i] +=1

max_common = max(common)
print(max_common)