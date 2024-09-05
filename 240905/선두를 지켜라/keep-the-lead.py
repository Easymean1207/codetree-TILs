# A,B -> N번, M동 이동
N,M = tuple(map(int, input().split()))

# A의 현재 위치, A의 행동 반경
A_current = 0
A_moves = []
for _ in range(N):
    # A의 속력(v), A가 이동한 시간 (t)
    v,t = list(map(int, input().split()))
    
    # 매 초마다 위치 기록
    for second in range(t):
        A_current = A_current + v
        A_moves.append(A_current)

# B의 현재 위치, B의 행동 반경
B_current = 0
B_moves = []
for _ in range(M):
    # B의 속력(v), A가 이동한 시간 (t)
    v,t = list(map(int, input().split()))

    # 매 초마다 위치 기록
    for second in range(t):
        B_current = B_current + v
        B_moves.append(B_current)

# print(A_moves)
# print(B_moves)

overtake_cnt = 0
current_leader = None

for t in range(len(A_moves)):
    if A_moves[t] > B_moves[t]:
        new_leader = 'A'
    elif B_moves[t] > A_moves[t]:
        new_leader = 'B'
    else:
        new_leader = None

    if new_leader != current_leader:
        if new_leader is not None:
            overtake_cnt += 1
        current_leader = new_leader

# 처음 선두를 잡았을 경우를 제외
overtake_cnt -=1

print(overtake_cnt)