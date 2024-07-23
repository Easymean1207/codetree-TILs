# 요청의 개수 : q
''' 요청의 종류
    1. 가장 앞에 있던 문자를 가장 뒤로
    2. 가장 뒤에 있던 문자를 가장 앞으로
    3. 문자열을 좌우로 뒤집기
 '''
word, queries = input().split()
queries = int(queries)

for _ in range(queries):
    query = int(input())

    if query == 1:
        word = word[1:] + word[0]
    elif query == 2:
        word = word[-1] + word[:-1]
    elif query == 3:
        word = word[::-1]
    else:
        print('잘못된 입력입니다.')
        continue
    
    print(word)