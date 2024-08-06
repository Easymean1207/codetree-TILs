def findKthWords(words, key, target_seq):
    # key로만 시작하는 단어들로 필터링
    filterd_words = [word for word in words if word.startswith(key)]

    # 단어 정렬
    filterd_words.sort()
        
    # k번째 단어 출력
    return filterd_words[k-1]
    


n, k, T = input().split()
n, k = int(n), int(k)

words = [
    input()
    for _ in range(n)
]

result = findKthWords(words, T , k)
print(result)