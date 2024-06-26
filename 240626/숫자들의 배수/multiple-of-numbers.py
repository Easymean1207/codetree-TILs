_list = []
n = int(input())
cnt = 0
multiple = 1

if(n < 1 or n > 10):
    print('정수의 범위는 1~10이어야 합니다.')
    exit(1)

while True:
    current = n * multiple
    _list.append(current)

    if current % 5 == 0:
        cnt+=1
        if cnt == 2:
            break
       
    multiple += 1

print(*_list)