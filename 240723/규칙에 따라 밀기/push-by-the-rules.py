# 문자열 A
# 명령: L(왼쪽으로 한 칸 밈) or R(오른쪽으로 한 칸 밈)

A = input()
cmd_list = input()

for cmd in cmd_list:
    # 왼쪽으로 한 칸 밈
    if cmd == 'L':
        A = A[1:] + A[0]
    elif cmd == 'R':
        A = A[-1] + A[:-1]
    else:
        print('Wrong command')
        continue

print(A)