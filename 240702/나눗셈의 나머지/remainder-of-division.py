a,b = list(map(int,input().split()))

mods = [0 for i in range(b)]
result = 0

while True:
    a, current_mod = int(a/b), int(a%b)
       
    mods[current_mod]+=1

    if a==0:
        break

for i in range(len(mods)):
    if mods[i] != 0:
        result+=mods[i]**2

print(result)