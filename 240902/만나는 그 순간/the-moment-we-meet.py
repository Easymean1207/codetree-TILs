# A는 N번, B는 M번
# 1초에 1m씩 움직임
N, M = tuple(map(int, input().split()))

A_moves = []
for _ in range(N):
    d, t = input().split()
    A_moves.append((d, int(t)))

B_moves = []
for _ in range(M):
    d, t = input().split()
    B_moves.append((d, int(t)))

A_positions = []
B_positions = []

a_cur = 0
b_cur = 0

for direction, time in A_moves:
    for _ in range(time):
        if direction == 'L':
            a_cur -=1
        elif direction == 'R':
            a_cur +=1
        A_positions.append(a_cur)

for direction, time in B_moves:
    for _ in range(time):
        if direction == 'L':
            b_cur -= 1
        elif direction == 'R':
            b_cur += 1
        B_positions.append(b_cur)

meeting_time = -1
for t in range(len(A_positions)):
    if A_positions[t] == B_positions[t]:
        meeting_time = t + 1
        break

print(meeting_time)
# print(A_positions)
# print(B_positions)