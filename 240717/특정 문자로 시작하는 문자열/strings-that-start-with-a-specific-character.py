n = int(input())

words = [
    input()
    for _ in range(n)
]

key = input()

# 조건에 만족하는 문자열을 저장할 리스트 생성
results = []

# 루프문을 돌며 result를 채움.
for word in words:
    if word[0] == key:
        results.append(word)

# 문자열의 개수, 총 길이 선언
total_cnt = len(results)
total_length = 0

for result in results:
    total_length += len(result)

avg_length = round(total_length/total_cnt, 2)

print(total_cnt, f"{avg_length:.2f}")