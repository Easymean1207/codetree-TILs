n = int(input())
S = input()

# Please write your code here.
Cs = []
Os = []
Ws = []
count = 0

def storeIndex(src, dst, target):
    for i, char in enumerate(src):
        if char == target:
            dst.append(i)

storeIndex(S, Cs, 'C')
storeIndex(S, Os, 'O')
storeIndex(S, Ws, 'W')

for C in Cs:
    for O in Os:
        for W in Ws:
            if C < O and O < W:
                count+=1

print(count)