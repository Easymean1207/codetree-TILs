a,b = list(map(int,input().split()))

mods = [0 for i in range(b)]
result = 0

while True:
    current_mod = a % b
       
    mods[current_mod]+=1
    a = a // b

    if a<=1:
        break

for i in range(len(mods)):
    if mods[i] != 0:
        result+=mods[i]**2

print(result)