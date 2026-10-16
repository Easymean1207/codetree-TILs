n, t = map(int, input().split()) # N r N의 격자, T초
r, c, d = input().split() #  D: U, D, R, L 중 하나
r, c = int(r), int(c) # R행 C열에 위치

# Please write your code here.
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
#     R  D   L   U

mappedDirections = {
    'R': 0,
    'D': 1,
    'L': 2,
    'U': 3
}

def in_range(r,c):
    return r >= 1 and r <= n and c >= 1 and c <= n

direction = mappedDirections[d]

for _ in range(t):
    nr, nc = r + dr[direction], c + dc[direction]

    if(in_range(nr, nc)): # 격자를 벗어나지 않음(벽에 만나지 않음)
        r, c = nr, nc
    else: # 격자를 벗어남(벽에 만남)
        direction = (direction + 2) % 4 # 방향 전환

print(r, c)