n = int(input())
nums = list(map(int, input().split()))

result = []

# 초기 최대 값, 인덱스 구하기
init_max = max(nums)
init_max_idx = nums.index(init_max)

# 결과 리스트에 (초기 최대 값의 인덱스 + 1) 추가
result.append(init_max_idx+1)

# 현재 최대 값의 인덱스
current_max_idx = init_max_idx

while current_max_idx > 0:
    # 0 ~ 최대 값 인덱스-1 범위의 임시 리스트 생성
    temp_ls = nums[:current_max_idx]
    
    # 임시 리스트의 최대 값, 인덱스 구하기
    max_value = max(temp_ls)
    max_index = temp_ls.index(max_value)
    
    # 결과 리스트에 (최대 값 인덱스 + 1)추가
    result.append(max_index+1)

    # 최대 값 인덱스 갱신
    current_max_idx = max_index


print(*result)