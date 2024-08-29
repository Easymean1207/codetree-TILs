# 숫자의 개수 N
N = int(input())

# 결과값이 될 증가 연속 부분의 수열 길이, 현재 증가 연속 부분 수열 길이, 전체 수열 선언
result = 0
current = 0
sequence = []

for i in range(N):
    num = int(input())
    sequence.append(num)

for i in range(len(sequence)):
    # 증가하는 연속 부분 수열에 해당하는 경우 -> current를 1 증가 
    if i == 0 or sequence[i] > sequence[i-1]:
        current +=1
    # 증가하는 연속 부분 수열에 해당하지 않는 경우 -> result 갱신, current를 1로 초기화
    else:
        result = max(current, result)
        current = 1

result = max(current, result)
print(result)