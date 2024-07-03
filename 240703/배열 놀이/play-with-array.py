# 원소 개수 n
# 질의 개수 q

# 질의는 "l a", "2 b", "3 s e" 중 하나
    # 1 a -> a 번째 원소 출력
    
    # 2 b -> b인 원소를 찾아 인덱스 출력
        # b가 여러 개라면 가장 작은 인덱스 출력
        # 원소가 없으면 0을 출력

    # 3 s e -> s부터 e번째 원소까지 공백으로 구분하여 출력

n,q = map(int, input().split())
elements = list(map(int, input().split()))

results = []

for i in range(q):
    input_query = list(map(int, input().split()))

    if input_query[0] == 1:
        a = input_query[1]
        results.append(elements[a-1])

    elif input_query[0] == 2:
        b = input_query[1]
        if b in elements:
            results.append(elements.index(b)+1)
        else:
            results.append(0)

    elif input_query[0] == 3:
        s = input_query[1]
        e = input_query[2]

        selected_elements = elements[s-1:e]
        changed = " ".join(map(str, selected_elements))
        
        results.append(changed)
        
    else:
        raise Exception('잘못된 종류의 질의입니다.')
    
for result in results:
    print(result)