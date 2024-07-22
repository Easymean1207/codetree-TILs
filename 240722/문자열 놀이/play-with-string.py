# 문자열 s, 질의의 개수 q
# 질의 1 : 1 a b -> a번째 문자와 b번째 문자를 교환
# 질의 2 : 2 a b -> 문자 a를 전부 문자 b로 변환

# 문자열 s, 질의 개수 q
s,q = input().split()
q = int(q)

# 문자열을 리스트로 변환
arr = list(s)

for i in range(q):
    query = input().split()
    
    # a번째 문자와 b번째 문자를 교환
    if query[0] == '1':
        a = int(query[1])-1
        b = int(query[2])-1
        arr[a],arr[b] = arr[b], arr[a]
        
        s = ''.join(arr)
        print(s)

    # 문자 a를 전부 문자 b로 변환
    elif query[0] == '2':
        a = query[1]
        b = query[2]

        for i in range(len(arr)):
            if arr[i] == a:
                arr[i] = b

        s = ''.join(arr)
        print(s)