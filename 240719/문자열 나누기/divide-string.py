n = input()

# 리스트 형태로 입력받음
num_ls = list(input().split())

# 리스트를 공백 제거한 문자열로 변환
num_str = ''.join(num for num in num_ls)

new_line_added = ''

# 5번째 element마다 줄 바꿈
for i in range(len(num_str)):
    new_line_added += num_str[i]
    if i % 5 == 4:
        new_line_added += '\n'

print(new_line_added)