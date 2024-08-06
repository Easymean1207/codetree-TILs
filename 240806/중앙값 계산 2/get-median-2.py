def printMedian(nums):
    for i in range(0, len(nums), 2):
        # 각 루프의 현재 숫자 배열 설정 및 정렬
        current_ls = nums[:i+1]
        current_ls.sort()

        # 각 루프의 중앙값 출력
        print(current_ls[len(current_ls)//2], end = ' ')


n = int(input())
nums = list(map(int, input().split()))

printMedian(nums)