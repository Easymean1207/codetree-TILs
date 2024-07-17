# n = 문자열 개수
n = int(input())

words = [
    input()
    for _ in range(n)
]

# 문자열 길이의 총합, a 등장 횟수 카운트 변수 선언
total_length = 0
cnt = 0

for word in words:
    total_length += len(word)

    if 'a' in word:
        cnt += word.count('a')

print(total_length, cnt)