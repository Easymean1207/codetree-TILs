idx = 0
results = []

while True:
    string = input()
    idx += 1

    if string == '0':
        break

    results.append(string)

print(len(results))

for i, result in enumerate(results):
    if i%2 == 0:
        print(result)