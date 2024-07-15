# n = 격자의 크기, m = 점의 개수
n, m = map(int, input().split())

# 기본 격자(nxn) 설정
placed= [
    [0 for _ in range(n)]
    for _ in range(n)
]

# 각 행,열에 값 할당
for _ in range(m):
    r,c = map(int, input().split())
    placed[r-1][c-1] = r * c

# 격자 출력

for row in placed:
    print(*row)