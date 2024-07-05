element_cnt = int(input())
elements = list(map(int, input().split()))

# 입력 값 정렬
elements.sort()

# 중복 원소 리스트 생성 (중복 값 제거를 위함)
already_exist = [x for i, x in enumerate(elements) if i != elements.index(x)]

# 중복 원소를 제거한 리스트로 변경
elements = [x for x in elements if x not in already_exist]

# 리스트 개수에 따른 조건문 설정
if not elements:
    print(-1)

else:
    print(max(elements))