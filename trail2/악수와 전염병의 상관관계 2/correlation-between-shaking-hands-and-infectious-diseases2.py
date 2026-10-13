# N명의 개발자
# 전염 가능한 횟수 : K번
# 최초 감염자 : P번 개발자
# T개의 악수기록: (t초에, x번 개발자, y번 개발자) 악수

N, K, P, T = map(int, input().split())
handshakes = [tuple(map(int, input().split())) for _ in range(T)]

infected = [0] * (N + 1)
infected[P] = 1; # P번 개발자는 최초 감염

prevShakeCount = [0] * (N + 1)
handshakes.sort() # 악수는 시간 순서대로 처리됨

for t, x, y in handshakes:
    # 악수 전 감염 상태를 저장
    x_status = infected[x]
    y_status = infected[y]
    
    # 감염된 상태이고 전염 가능한 상태라면(이전 악수횟수가 K번 미만) 상대 전염
    if x_status == 1 and prevShakeCount[x] < K:
        infected[y] = 1

    if y_status == 1 and prevShakeCount[y] < K:
        infected[x] = 1

    # 악수 이전에 감염자였다면 악수 횟수 1 추가
    if x_status == 1:
        prevShakeCount[x] += 1

    if y_status == 1:
        prevShakeCount[y] += 1

# 최종 감염 여부 출력
for i in range(1, N + 1):
    print(infected[i], end='')
    

