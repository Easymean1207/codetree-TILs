# 수열 A -> n1개의 원소, 수열 B -> n2개의 원소
# 연속부분수열 -> 수열 A의 원소들을 연속하게 뽑았을 때, 수열 B라면 성립
    # ex) 수열 A = [1,5,2,6] 수열 B = [5,2] -> ok
    #     수열 A = [1,5,2,6] 수열 B = [5,6] -> X

n1, n2 = map(int, input().split())

A_seq = list(map(int, input().split()))
B_seq = list(map(int, input().split()))

for i in range(len(A_seq)):
    if A_seq[i] == B_seq[0]:
            for k in range(1, len(B_seq)):
                if A_seq[i+1] != B_seq[k]:
                    print('No')
                    break
                else:
                    print('Yes')
                    break
            break    
    else:
        print('No')
        break