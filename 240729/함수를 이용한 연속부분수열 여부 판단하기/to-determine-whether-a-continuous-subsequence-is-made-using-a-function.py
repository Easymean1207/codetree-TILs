''' 부분 문자열인지 확인하는 함수 '''

# 방법1: 수열을 문자열로 변환 후 메서드 이용
def isContinuousSub(main, target):
    # 숫자 리스트를 문자열로 변환
    main = ''.join(map(str, main))
    target = ''.join(map(str, target))

    # find() 메서드로 확인
    if main.find(target) != -1:
        return True
    else:
        return False

# 방법2: 수열끼리 직접 비교
def isContinuousSub2(main, target):
    len_main = len(main)
    len_target = len(target)

    if len_target > len_main:
        return False

    # 부분 수열인지 확인
    # 0번 index부터 (수열 길이 - 부분 수열 길이)의 인덱스까지
    # 같은 값이 없으면 부분 수열의 후보조차 성립 X 
    for i in range(len_main - len_target + 1):
        if main[i:i+len_target] == target:
            return True

    return False


n1, n2 = tuple(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = isContinuousSub(A,B)
result2 = isContinuousSub2(A,B)

print('Yes' if result2 == True else 'No')