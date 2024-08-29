# 수열의 길이 n, 정수 t
n,t = tuple(map(int, input().split()))

# 전체 수열
sequence = list(map(int, input().split()))

# 현재 길이, 최종 길이
current = 0
result = 0

for i in range(len(sequence)):
    # 해당 인덱스의 값이 t보다 큰 경우 -> current 1 증가
    if sequence[i] > t:
        current +=1
        # print(f"t보다 큼 : idx:{i}, value:{sequence[i]}, cur:{current}")
    # 해당 인덱스의 값이 t보다 작거나 같은 경우 -> result 갱신, current를 0로 초기화
    else:
        # print(f"t보다 작거나 같음 : idx:{i}, value:{sequence[i]}, cur:{current}")
        result = max(result, current)
        # print(f"result:{result}")
        current = 0
    
result = max(result, current)
print(result)