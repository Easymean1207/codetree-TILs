word = input()

n = int(input())

results = word[len(word):len(word)-n-1:-1]
print(results)