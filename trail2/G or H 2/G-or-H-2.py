n = int(input())
people = [tuple(input().split()) for _ in range(n)]
pos = [int(p[0]) for p in people]
alpha = [p[1] for p in people]

# Please write your code here.
MAX_RANGE = 100
maxLength = 0 # 사진의 최대 크기

# 각 위치에 G/H 기록
record = [0] * (MAX_RANGE +1)
for each_pos, char in zip(pos, alpha):
    record[each_pos] = char


for i in range(MAX_RANGE+1): # 시작점
    for j in range(i+1, MAX_RANGE+1): # 끝점
        gCount = 0
        hCount = 0

        # 사진의 크기는 양 끝에 있는 두 사람의 거리
        # -> 양 끝에는 사람이 무조건 있어야 함
        if record[i] == 0 or record[j] == 0:
            continue

        # i ~ j 구간의 G, H 개수 확인
        for k in range(i, j + 1):
            if record[k] == 'G':
                gCount += 1
            elif record[k] == 'H':
                hCount += 1
        
        # print(hCount, gCount)

        if hCount == 0 or gCount == 0 or hCount == gCount:
            maxLength = max(maxLength, j-i)

print(maxLength)

    