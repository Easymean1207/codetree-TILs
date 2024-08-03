def gcd(a,b):
    while b > 0:
        a, b = b, a%b
    return a


def lcm(a,b):
    return a * b // gcd(a,b)

# 각 재귀 당 2개의 원소를 묶어 그 재귀에서의 lcm 도출
def multi_lcm(nums):
    # 종료 조건: 원소가 하나면 최소공배수는 그 원소 자체가 됨.
    if len(nums) == 1:
        return nums[0]
    
    # 재귀 호출
    return lcm(nums[0], multi_lcm(nums[1:]))


n = int(input())
nums = list(map(int, input().split()))

print(multi_lcm(nums))