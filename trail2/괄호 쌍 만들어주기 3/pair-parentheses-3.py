A = input()

# Please write your code here.
startPoint = 0
endPoint = len(A)+1
count = 0

for i in range(len(A)):
    if A[i] == '(':
        startPoint = i

        for j in range(i+1, len(A)):
            if A[j] == ')':
                endPoint = j
                count +=1
                # print(startPoint, endPoint, count)

print(count)