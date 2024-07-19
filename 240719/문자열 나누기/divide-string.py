n = input()

# 리스트 형태로 입력받음
num_ls = list(input().split())

num_str = ''.join(num for num in num_ls)

new_line_added = ''

for i in range(len(num_str)):
    new_line_added += num_str[i]
    if i % 5 == 4:
        new_line_added += '\n'

print(new_line_added)