def calculateElapsedTime(start_h, start_m, end_h, end_m):
    elasped_time = 0
    
    while True:
        if start_h == end_h and start_m == end_m:
            break
        
        elasped_time +=1
        start_m +=1

        if start_m == 60:
            start_h += 1
            start_m = 0

    return elasped_time


start_hour, start_minute, end_hour, end_minute = list(map(int, input().split()))

elasped_time = calculateElapsedTime(start_hour,start_minute,end_hour,end_minute)
print(elasped_time)