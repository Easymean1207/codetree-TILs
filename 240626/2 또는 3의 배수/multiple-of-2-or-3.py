n = int(input())
ls = []

# make ls
for i in range(1, n+1):
    if(i % 2 == 0 or i % 3 == 0):
        ls.append(1)
    else:
        ls.append(0)

# print ls
for i in range(len(ls)):
    print(ls[i], end = ' ')