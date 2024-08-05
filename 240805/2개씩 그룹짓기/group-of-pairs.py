def groupingAndFind(nums):
    # 먼저 입력 숫자 리스트를 sorting
    sorted_nums = sorted(nums)
    # 초기 최대값을 0으로 설정
    biggest = 0

    # 2개씩 그룹을 짓기 때문에 절반까지만 비교하면 됨.
    for i in range(int(len(sorted_nums)/2)):
        # 각 루프에서 처음 원소와 마지막 원소의 합을 후보군으로 지정
        candidate = sorted_nums[i] + sorted_nums[-(i+1)]
        # 현재 최대값과 비교
        biggest = max(biggest, candidate)
        
    return biggest


group_nums = int(input())
nums = list(map(int,input().split()))

result = groupingAndFind(nums)
print(result)