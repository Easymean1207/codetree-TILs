n = int(input())

concat_str = ''

for _ in range(n):
    word = input()
    concat_str = ''.join([concat_str, word])

print(concat_str)