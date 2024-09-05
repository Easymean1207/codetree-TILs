def has_overtaken(A_pos_prev, B_pos_prev, A_pos_curr, B_pos_curr):

    return (A_pos_prev >= B_pos_prev and A_pos_curr < B_pos_curr) \
            or (A_pos_prev <= B_pos_prev and A_pos_curr > B_pos_curr)

# A,B -> N번, M동 이동

N,M = tuple(map(int, input().split()))

# A의 행동 반경을 리스트에 추가
A_moves = []
for _ in range(N):
    # A의 속력(v), A가 이동한 시간 (t)
    v,t = input().split()
    A_moves.append((int(v),int(t)))

# B의 행동 반경을 리스트에 추가
B_moves = []
for _ in range(M):
    # B의 속력(v), A가 이동한 시간 (t)
    v,t = input().split()
    B_moves.append((int(v),int(t)))

# A,B의 실제 이동값
A_positions = []
B_positions = []

# 각 현재 위치 설정
A_current = 0
B_current = 0

for velocity, times in A_moves:
    for _ in range(times):
        A_current += velocity
        A_positions.append(A_current)

for velocity, times in B_moves:
    for _ in range(times):
        B_current += velocity
        B_positions.append(B_current)

# print(A_positions)
# print(B_positions)

overtake_cnt = 0

for t in range(1, len(A_positions)):
    if has_overtaken(A_positions[t-1], B_positions[t-1], A_positions[t], B_positions[t]):
        overtake_cnt += 1
        
print(overtake_cnt)