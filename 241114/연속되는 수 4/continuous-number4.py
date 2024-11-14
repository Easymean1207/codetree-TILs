# 숫자의 개수 N
N = int(input())

# 결과값이 될 연속 부분 수열 길이, 현재 연속 부분 수열 길이, 전체 수열 선언
sequence = [
    int(input())
    for _ in range(N)
]

result = 0
current_cnt = 0

for i in range(len(sequence)):
    # 증가하는 연속 부분 수열에 해당 -> current_cnt 1 증가
    if i == 0 or sequence[i] > sequence[i-1] :
        current_cnt +=1
    
    #  # 증가하는 연속 부분 수열에 해당하지 않는 경우 -> current_cnt를 1로 초기화
    else:
        current_cnt = 1
    
    result = max(current_cnt, result)

print(result)