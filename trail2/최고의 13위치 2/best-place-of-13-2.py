n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

coinCount = 0

def in_range(r, c):
    return (r>=0 and r<n) and (c>=0 and c<n)


for r1 in range(n):
    for c1 in range(n-2):
        
        for r2 in range(n):
            for c2 in range(n-2):
                
                # 직사각형은 서로 겹치면 안됨
                if r1 == r2 and abs(c1- c2) <=2:
                    continue
                
                # 각 직사각형의 코인 갯수
                coin1 = arr[r1][c1] + arr[r1][c1+1] + arr[r1][c1+2]
                coin2 = arr[r2][c2] + arr[r2][c2+1] + arr[r2][c2+2]

                # 코인의 최대값 갱신
                coinCount = max(coinCount, coin1+coin2)


print(coinCount)
            
        