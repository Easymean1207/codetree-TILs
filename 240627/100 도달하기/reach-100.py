n = int(input())
ls = [1,n,]

i = 0
while True:
    new_value = ls[i] +ls[i+1]
    ls.append(new_value)
    
    i+=1

    if new_value > 100:
        break

print(*ls)