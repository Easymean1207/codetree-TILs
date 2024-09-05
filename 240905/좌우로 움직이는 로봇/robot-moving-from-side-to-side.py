# 1초에 1칸씩 움직임
# A가 움직이는 횟수 n, B가 움직이는 횟수 m
n,m = tuple(map(int, input().split()))

# A의 현재위치, 이동 정보
a_current = 0
A_moves = []
for _ in range(n):
    # A가 움직인 시간(t), A가 움직인 방향(d)
    t, d = input().split()
    t = int(t)
    
    for second in range(t):
        if d == 'L':
            a_current -= 1
            A_moves.append(a_current)
        
        if d == 'R':
            a_current += 1
            A_moves.append(a_current)


b_current = 0
B_moves = []
for _ in range(m):
    # B가 움직인 시간(t), B가 움직인 방향(d)
    t, d = input().split()
    t = int(t)
    
    for second in range(t):
        if d == 'L':
            b_current -= 1
            B_moves.append(b_current)
        
        if d == 'R':
            b_current += 1
            B_moves.append(b_current)

# print(A_moves)
# print(B_moves)

# 하나의 로봇이 먼저 움직임을 끝냈을 때, 끝난 위치를 다른 로봇의 움직임이 끝날 때까지 유지
end_first = min(len(A_moves),len(B_moves))
end_last = max(len(A_moves),len(B_moves))

if len(A_moves) < len(B_moves):
    for idx in range(end_first, end_last):
        A_moves.append(A_moves[-1])
elif len(A_moves) > len(B_moves):
    for idx in range(end_first, end_last):
        B_moves.append(B_moves[-1])

meeting_cnt = 0
for i in range(1, end_last):
    if A_moves[i-1] != B_moves[i-1] and A_moves[i] == B_moves[i]:
        meeting_cnt+=1

print(meeting_cnt)