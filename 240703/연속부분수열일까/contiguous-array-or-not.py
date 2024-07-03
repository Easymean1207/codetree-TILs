# 수열 A -> n1개의 원소, 수열 B -> n2개의 원소
# 연속부분수열 -> 수열 A의 원소들을 연속하게 뽑았을 때, 수열 B라면 성립
    # ex) 수열 A = [1,5,2,6] 수열 B = [5,2] -> ok
    #     수열 A = [1,5,2,6] 수열 B = [5,6] -> X

n1, n2 = map(int, input().split())

A_seq = list(map(int, input().split()))
B_seq = list(map(int, input().split()))

is_sub = False

# n1-n2 사이에 B_seq[0]의 값이 없다면 애초에 연속부분수열이 성립하지 않음.
for i in range(n1-n2+1):
    # 일치값부터 B_seq 길이의 리스트만큼 list slicing 후 B_seq와 비교
    if A_seq[i:i+n2] == B_seq:
        is_sub = True
        break
        
if is_sub:
    print("Yes")
else:
    print("No")