dices = [0 for i in range(6)]

results = list(map(int, input().split()))

for result in results:
    if (result >= 1 and result <= 6):
        dices[result - 1] += 1

for i in range(len(dices)):
    print(f'{i+1} - {dices[i]}')