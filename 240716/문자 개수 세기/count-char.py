word = input()
key = input()

cnt = 0

for alphabet in word:
    if alphabet == key:
        cnt+=1

print(cnt)