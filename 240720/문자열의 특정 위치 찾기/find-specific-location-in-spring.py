word, key = input().split()

location = word.find(key)

print('No' if location == -1 else location)