# 문자열의 길이: L
word = input()
L = len(word)

print(word)
for i in range(1,L+1):
    word = word[-1] + word[:-1]
    print(word)