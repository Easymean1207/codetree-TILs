from typing import List

class Date:
    def __init__(self, month:int, day:int):
        self.month, self.day = month, day

def calculateElaspedDay(start:Date, end:Date) -> int:
    elapsed_day = 1
    num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    while True:
        if start.month == end.month and start.day == end.day:
            break

        elapsed_day+=1
        start.day+=1

        if start.day > num_of_days[start.month]:
            start.month +=1
            start.day =1
    
    return elapsed_day


m1, d1, m2, d2 = tuple(map(int,input().split()))

start_date = Date(m1, d1)
end_date = Date(m2, d2)

elapsed_day = calculateElaspedDay(start_date, end_date)
print(elapsed_day)