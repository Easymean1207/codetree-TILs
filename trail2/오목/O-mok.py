board = [list(map(int, input().split())) for _ in range(19)]

# Please write your code here.

# 오른쪽, 아래쪽, 오른쪽 아래 대각선, 왼쪽 아래 대각선 
dr = [0, 1, 1, 1]
dc = [1, 0, 1, -1]

winner = 0 # 어떤 돌이 이겼는지는 아직 모름

def in_range(r, c):
    return (r>=0 and r<19) and (c>=0 and c<19)


for r in range(19):
    for c in range(19):
        # 빈칸인 경우 스킵
        if board[r][c] == 0:
            continue
        
        # 방향 별로 오목이 완성되었는지 체크
        for direction in range(4):
            isFive = True

            # 현재 돌을 제외한 나머지 4개 확인
            for step in range(1, 5):
                nr = r + dr[direction] * step
                nc = c + dc[direction] * step

                # 바둑판을 벗어나면 해당 스텝 루프 탈출
                if not in_range(nr,nc):
                    isFive = False
                    break

                # 색이 다르면 해당 스텝 루프 탈출
                if board[r][c] != board[nr][nc]:
                    isFive = False
                    break
            
            # 오목이 완성된 색의 가운데 좌표
            if isFive:
                winner = board[r][c]
                middleR = r + dr[direction] * 2
                middleC = c + dc[direction] * 2
                break
        
        if winner != 0:
            break
    
    if winner != 0:
            break

if isFive:
    print(winner)
    print(middleR + 1 , middleC + 1)
else:
    print(winner)