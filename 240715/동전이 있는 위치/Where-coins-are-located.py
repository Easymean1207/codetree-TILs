# n = 격자의 크기, m = 동전의 개수
n, m = map(int, input().split())

# 기본 격자 설정
placed = [
    [0 for _ in range(n)]
    for _ in range(n)
]

# 동전 위치 설정(r행 c열) 
for _ in range(m):
    r, c = tuple(map(int, input().split()))
    placed[r-1][c-1] = 1

for row in placed:
    print(*row)