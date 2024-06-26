n = int(input())
_list = list(map(int, input().split()))
even_list = []

if n != len(_list):
    print("n과 리스트의 개수가 일치하지 않습니다.")
    exit(1)

even_list = [item for item in _list if item %2 == 0]

print(*even_list)