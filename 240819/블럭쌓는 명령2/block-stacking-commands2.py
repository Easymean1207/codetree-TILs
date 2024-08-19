# N개의 칸, K번의 명령
N,K = tuple(map(int, input().split()))

stacked = [0 for i in range (N)]

for i in range(K):
    # 시작점, 끝점 입력 받기
    start,end = tuple(map(int, input().split()))
    
    # 시작점 ~ 끝 채우기
    for j in range(start, end+1):
        stacked[j]+=1

print(max(stacked))