def lexicographical(words):
    return words.sort()


n = int(input())
words = [
    list(input())
    for _ in range(n)
]

lexicographical(words)

words = [''.join(word) for word in words]

for word in words:
    print(word)