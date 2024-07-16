word1, word2 = input().split()

len1 = len(word1)
len2 = len(word2)

if len1 > len2:
    print(f'{word1} {len1}')
elif len1 < len2:
    print(f'{word2} {len2}')
else:
    print('same')