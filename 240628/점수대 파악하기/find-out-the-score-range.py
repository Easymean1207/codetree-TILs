scores = list(map(int, input().split()))
markers = [0 for _ in range(10)]

for score in scores:
    if score == 0:
        break
    if score >= 10:
        mark = score // 10
        markers[mark-1] += 1

markers.reverse()

for i in range(len(markers)):
    print(f'{10 * (10-i)} - {markers[i]}')