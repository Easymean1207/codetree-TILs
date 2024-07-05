element_cnt = int(input())
# elements = list(map(int, input().split()))
elements = [3,2,3,1]

elements.sort()

already_exist = [x for i, x in enumerate(elements) if i != elements.index(x)]
# print(already_exist)

elements = [x for x in elements if x not in already_exist]

# print(*elements)

if not elements:
    print(-1)

else:
    print(max(elements))