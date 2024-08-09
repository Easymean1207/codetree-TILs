class Time:
    def __init__(self, month, day, hour, minute):
        self.month,self.day = month, day
        self.hour,self.minute = hour, minute


def calculateElapsedTime(start, end):
    # 11일 이전인 경우
    if start.day > end.day:
        return -1

    # 11인 경우, 시간과 분을 비교
    elif start.day == end.day:
        if (start.hour, start.minute) > (end.hour, end.minute):
            return -1
    
    elapsed_time = 0
    
    while True:
        if start.day == end.day and start.hour == end.hour and start.minute == end.minute:
            break
    
        # 분 -> 시간 -> 날짜 순으로 로직 업데이트
        elapsed_time +=1
        start.minute +=1

        # 분(minute)을 시간(hour)으로 치환
        if start.minute == 60:
            start.minute = 0
            start.hour +=1
        
        # 시간(hour)을 일(day)로 치환
        if start.hour == 24:
            start.hour = 0
            start.day+=1
        
    return elapsed_time
        
            
given_day, given_hour, given_minute = tuple(map(int, input().split()))
start_date = Time(11, 11, 11, 11)
end_date = Time(11, given_day, given_hour, given_minute)

elapsed_time = calculateElapsedTime(start_date, end_date)
print(elapsed_time)