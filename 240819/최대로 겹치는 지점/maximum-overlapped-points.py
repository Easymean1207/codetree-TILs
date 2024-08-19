# 최대 범위 지정
MAX_RANGE = 100

# 선분의 개수 n
n = int(input())

# 각 구간에 대한 정보
segments = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

# 0 ~ 100까지의 범위
common = [0 for _ in range (MAX_RANGE+1)]

# 각 구간에 대한 정보를 배열에 추가
for x1, x2 in segments:
    # 구간이 아닌 점이라서 [x1, x2]의 범위를 가져댜 함.
    for i in range(x1, x2+1):
        common[i] +=1

max_common = max(common)
print(max_common)