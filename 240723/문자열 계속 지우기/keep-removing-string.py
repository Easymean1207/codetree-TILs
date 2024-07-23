# 문자열 A, 문자열 B
A = input()
B = input()

while B in A:
    # A 안에 있는 substring B의 위치 찾기
    index = A.find(B)
    
    # slicing으로 B 제거
    A = A[:index]+A[index+len(B):]

print(A)