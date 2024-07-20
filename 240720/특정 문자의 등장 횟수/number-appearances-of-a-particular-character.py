word = input()

key1 = 'ee'
key2 = 'eb'

key1_cnt = 0

for i in range(len(word)-1):
    if word[i] == 'e' and word[i+1] == 'e':
        key1_cnt+=1

print(key1_cnt, word.count(key2))