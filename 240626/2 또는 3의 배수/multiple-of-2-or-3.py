n = int(input())
ls = []


# make ls
for i in range(1, n+1):
   make_ls = ls.append(1) if(i % 2 == 0 or i % 3 == 0) else ls.append(0)

# print ls
print(*ls)