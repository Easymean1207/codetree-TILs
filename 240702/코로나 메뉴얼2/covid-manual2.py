cold = []
temp = []
clinics = [0 for i in range(4)]

for i in range(3):
    info = input().split()
    
    cold.append(info[0])
    
    info[1] = int(info[1])
    temp.append(info[1])

# print(clinics)

for i in range(len(cold)):
    if cold[i] == 'Y':
        if temp[i] >= 37:
            clinics[0]+=1
        else:
            clinics[2]+=1
    else:
        if temp[i] >= 37:
            clinics[1]+=1
        else:
            clinics[3]+=1

if clinics[0]>=2:
    clinics.append('E')

print(*clinics)