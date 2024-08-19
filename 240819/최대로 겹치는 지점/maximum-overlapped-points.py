MAX_RANGE = 100
# 선분의 개수 n
n = int(input())

# 각 구간
segments = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

# 0 ~ 100까지의 범위
common = [0 for _ in range (MAX_RANGE+1)]

for x1, x2 in segments:
    for i in range(x1, x2+1):
        common[i] +=1

max_common = max(common)
print(max_common)