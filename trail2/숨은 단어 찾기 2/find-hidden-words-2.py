N, M = map(int, input().split())
arr = [input() for _ in range(N)]

# Please write your code here.

# 위, 오른쪽 위, 오른쪽, 오른쪽 아래,
# 아래, 왼쪽 아래, 왼쪽, 왼쪽 위
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

leeCount = 0

def in_range(r, c):
    return (r>=0 and r<N) and (c>=0 and c<M)


for r in range(N):
    for c in range(M):
        # 시작점이 L이 아닌 경우 스킵
        if arr[r][c] != 'L':
            continue
        
        # 방향 별로 'LEE'가 완성되었는지 체크
        for direction in range(8):
            isLee = True

            # 현재 칸을 제외한 나머지 2칸 확인
            for step in range(1, 3):
                nr = r + dr[direction] * step
                nc = c + dc[direction] * step

                # 격자를 벗어나면 해당 스텝 루프 탈출
                if not in_range(nr,nc):
                    isLee = False
                    break

                # 'E'가 아니라면 해당 스텝 루프 탈출
                if arr[nr][nc] != 'E':
                    isLee = False
                    break
            
            # lee의 갯수 하나 증가
            if isLee:
                leeCount +=1
                

print(leeCount)