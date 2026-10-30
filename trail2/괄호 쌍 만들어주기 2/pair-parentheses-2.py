A = input()

# Please write your code here.
openBracket = []
closeBracket = []
count = 0

# '((' 위치 확인
for i in range(len(A)-1):
    if A[i] == A[i+1] == '(':
        openBracket.append(i)

# '))' 위치 확인
for i in range(len(A)-1):
    if A[i] == A[i+1] == ')':
        closeBracket.append(i)

for open in openBracket:
    for close in closeBracket:
        if (open < close):
            count+=1

print(count)