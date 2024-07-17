words = input().split()

total_length = 0

for i in range(len(words)):
    total_length += len(words[i])

print(total_length)