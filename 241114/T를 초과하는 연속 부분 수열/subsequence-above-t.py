# 수열의 길이 n, 정수 t
n, t = tuple(map(int, input().split()))
# 전체 수열
sequence = list(map(int, input().split()))

# 현재 길이, 최종 길이
current = 0
result = 0

for i in range(len(sequence)):
    # 현재 값이 t보다 큼 -> currnet 1 증가
    if sequence[i] > t:
        current +=1
    # 현재 값이 t보다 작거나 같음 -> current를 0으로 초기화
    else:
        current = 0
    
    result = max(current, result)

print(result)
    