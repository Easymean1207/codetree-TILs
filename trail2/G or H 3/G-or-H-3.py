n, k = map(int, input().split())
x = []
c = []
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

# Please write your code here.
# 점수가 기록된 수직선
record = [0] * 10001
for pos, char in zip(x, c):
    if char == 'G':
        record[pos] = 1
    else:
        record[pos] = 2

# 수직선에서 범위내의 최대 점수
maxScore = 0
for start in range(0, 10000-k+1):
    currentScore = 0
    for pos in range(start, start+k+1): # [s, s+k] 범위
        currentScore += record[pos] # 현 범위에서의 점수

    maxScore = max(maxScore, currentScore) # 비교 후, 최대값 갱신

print(maxScore)