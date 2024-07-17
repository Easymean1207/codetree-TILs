words = [
    input()
    for _ in range(10)
]

key = input()

results = []

for word in (words):
    if word[-1] == key:
        results.append(word)

print('None' if not results else '\n'.join(results))