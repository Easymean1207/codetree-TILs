a = input()

# Please write your code here.
candidates = []

for i in range(len(a)):
    changed = list(a) # 값의 변경을 위해 리스트 상태의 a를 담을 변수 선언

    # i번째 회차에 i번째 인덱스의 비트 반전
    if changed[i] == '1':
        changed[i] = '0'
    else:
        changed[i] = '1'
    
    changed = int(''.join(changed), 2) # 10진수로 변환
    
    candidates.append(changed) # 변환된 결과를 후보군 배열에 추가

candidates.sort(reverse=True)
print(candidates[0])
