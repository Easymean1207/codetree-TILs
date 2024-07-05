element_cnt = int(input())
elements = list(map(int, input().split()))

elements.sort()

already_exist = [x for i, x in enumerate(elements) if i != elements.index(x)]

for element in elements:
    if element in already_exist:
        elements.remove(element)

if not elements:
    print(-1)

else:
    print(max(elements))