cnt = int(input())
_list = list(map(int, input().split()))

if cnt != len(_list):
    print("아이템 개수를 확인해주세요")
    exit(1)

new_list = [item ** 2 for item in _list]

print(*new_list)