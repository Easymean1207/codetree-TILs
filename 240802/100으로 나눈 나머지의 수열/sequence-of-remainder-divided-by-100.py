def fiboExponentMod(idx):
    if idx == 1:
        return 2
    elif idx == 2:
        return 4
    
    return (fiboExponentMod(idx-1) * fiboExponentMod(idx-2))%100


N = int(input())

print(fiboExponentMod(N))