# n = 격자의 크기, m = 점의 개수
n, m = map(int, input().split())

# 기본 격자 설정
placed = [
    [0 for _ in range(n)]
    for _ in range(n)
]

# 초기 값 설정
value = 1

# 해당 위치(r행 c열)에 값 할당
for _ in range(m):
    r, c = tuple(map(int, input().split()))
    placed[r-1][c-1] = value
    value+=1

# 격자 출력
for row in range(n):
    for col in range(n):
        print(placed[row][col], end = ' ')
    print()