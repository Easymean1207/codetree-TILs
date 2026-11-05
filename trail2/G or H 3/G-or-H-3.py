n, k = map(int, input().split())
x = []
c = []
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

# Please write your code here.
# 점수가 기록된 수직선
MAX_NUM = 10000

record = [0] * (MAX_NUM+1)
for pos, char in zip(x, c):
    if char == 'G':
        record[pos] = 1
    else:
        record[pos] = 2

# 수직선에서 범위내의 최대 점수
maxScore = 0
for i in range(MAX_NUM-k+1): # i(임의의 시작점 s)
    currentScore = 0
    for j in range(i, i+k+1): # [s, s+k] 범위
        currentScore += record[j] # 현 범위에서의 점수

    maxScore = max(maxScore, currentScore) # 비교 후, 최대값 갱신

print(maxScore)