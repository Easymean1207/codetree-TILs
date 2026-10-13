MAX_TIME = 1000;

n, m = map(int, input().split())

d = []
t = []
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))

# 각 위치 배열 및 시작 위치 선언
A_location = [0] * (MAX_TIME * n + 1)
B_location = [0] * (MAX_TIME * m + 1)
currentA = 1
currentB = 1

# print(d, t)
# print(d2, t2)

# A의 위치 기록
for i in range(n):
    if(d[i] == 'L'):
        for j in range(currentA, currentA + t[i]):
            A_location[j] = A_location[j-1] -1;
    elif(d[i] == 'R'):
        for j in range(currentA, currentA + t[i]):
            A_location[j] = A_location[j-1] +1;
    
    currentA = currentA + t[i]


# B의 위치 기록
for i in range(m):
    if(d2[i] == 'L'):
        for j in range(currentB, currentB + t2[i]):
            B_location[j] = B_location[j-1] -1;
    elif(d2[i] == 'R'):
        for j in range(currentB, currentB + t2[i]):
            B_location[j] = B_location[j-1] +1;
    
    currentB = currentB + t2[i]

# 최초로 만나는 시각 찾기
meetingTime = -1

shortestMovement = min(currentA, currentB)

for i in range(1, shortestMovement):
    if(A_location[i] == B_location[i]):
        meetingTime = i
        break

print(meetingTime)
