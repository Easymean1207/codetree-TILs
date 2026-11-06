N, K = map(int, input().split())
candy = []
pos = []

for _ in range(N):
    c, p = map(int, input().split())
    candy.append(c)
    pos.append(p)

# Please write your code here.
MAX = 400 # 범위 (-200(0) ~ 200(400))

maxCandy = 0

# 각 위치의 사탕 개수 저장(같은 위치에 여러 번 놓일 수 있음)
line = [0] * (MAX+1)
for c, p in zip(candy, pos):
    line[p] += c

for i in range(MAX+1):
    if i-K >= 0 and i+K <= MAX: # [i-k, i+k]가 유효 범위인지 확인
        currentCandy = 0

        for j in range(i-K, i+K+1):
            currentCandy += line[j]
        
        maxCandy = max(maxCandy, currentCandy)

print(maxCandy)