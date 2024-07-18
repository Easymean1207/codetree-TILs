A = input()

encoded = []
cnt = 1

for i in range(len(A)-1):
    # 다음 문자 == 지금 문자
    if A[i+1] == A[i]:
        cnt+=1
        continue

    # 다음 문자 != 지금 문자
    else:
        encoded.append((A[i], cnt))
        cnt = 1

# 마지막 문자열 추가
encoded.append((A[-1], cnt))

# encoded 리스트를 문자열로 변환
result = "".join(f'{char}{cnt}' for char, cnt in encoded)

print(len(result))
print(result)