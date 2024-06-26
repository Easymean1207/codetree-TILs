maximum = 100
_list = []
items = list(map(int, input().split()))


for i in range(len(items)):
    if(items[i] == 0):
        break
    if(items[i] %2 == 0):
        _list.append(items[i]//2)
    else:
        _list.append(items[i]+3)

if(len(items) > 100):
    print('최대 개수는 100개 입니다.')
    exit(1)

print(*_list)