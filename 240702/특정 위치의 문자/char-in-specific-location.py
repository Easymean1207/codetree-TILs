word = ['L', 'E', 'B', 'R', 'O', 'S']

search = input()

if search not in word:
    print('None')
else:
    print(word.index(search))