element_cnt = int(input())
elements = list(map(int, input().split()))

elements.sort(reverse=True)

print(elements[0], elements[1])