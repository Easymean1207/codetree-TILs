# 학생 수: N (1 ~ 100)
# K번(1 ~ 10000) 이상의 벌칙 -> 벌금
# M번(1 ~ 10000)에 걸쳐 학생의 번호가 주어짐

N,M,K = tuple(map(int, input().split()))

target_list = []
student = [0] * (N+1)
picked_number = -1

for _ in range(M):
    # 해당 회차 벌칙 횟수를 누적시킬 학생 번호 선정
    target = int(input())
    target_list.append(target)

    # student에 벌칙 정보를 갱신
    student[target]+=1

    # 조건 만족 시 반복문 종료
    if student[target] == K:
        picked_number = target
        break

print(picked_number)