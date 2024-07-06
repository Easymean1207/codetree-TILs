nums = list(map(int, input().split()))

bigger = [num for num in nums if num > 500]
smaller = [num for num in nums if num < 500]

print(max(smaller), min(bigger))