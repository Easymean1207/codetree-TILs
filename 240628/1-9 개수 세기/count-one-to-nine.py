n = int(input())
show_up_num = map(int, input().split())

count_arr = [0 for _ in range(9)]

for num in show_up_num:
    if num >= 1 and num <= 9:
        count_arr[num-1]+=1

for count in count_arr:
    print(count)