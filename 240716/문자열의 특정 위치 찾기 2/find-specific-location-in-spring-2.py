words = ['apple', 'banana', 'grape', 'blueberry', 'orange']

key = input()
values = []

for i, word in enumerate(words):
    if word[2] == key or word[3] == key:
        values.append(word)
            
for value in values:
    print(value)

print(len(values))