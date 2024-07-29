def isContinuousSub(main, target):
    # 리스트를 문자열로 변환, 구분자를 추가
    main = ','.join(map(str, main))
    target = ','.join(map(str, target))

    # find 메서드를 사용하여 target의 시작 인덱스 찾기
    if main.find(target) != -1:
        return True
    else:
        return False

# 사용자 입력 받기
n1, n2 = tuple(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 결과 출력
result = isContinuousSub(A, B)
print('Yes' if result else 'No')