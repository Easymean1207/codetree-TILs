first, second = map(int, input().split())

sequence = [first, second]

for i in range(8):
    new_value = sequence[i+1] + 2 * sequence[i]
    sequence.append(new_value)

print(*sequence)