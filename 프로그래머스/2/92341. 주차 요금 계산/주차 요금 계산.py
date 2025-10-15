# 기본시간(분) 기본요금 추가분당 추가요금
from math import ceil

def calc(fees, time):
    x,y,z,w = fees
    if time <= x:
        return y
    else:
        return y+ceil((time-x)/z)*w

def calctime(time1, time2):
    h1, m1 = map(int, time1.split(':'))
    h2, m2 = map(int, time2.split(':'))
    
    if m2-m1 >= 0:
        m3 = m2-m1
    else:
        h2 -= 1
        m3 = m2+60-m1
    
    return (h2-h1)*60 + m3
    

def solution(fees, records):
    records = list(map(lambda x:x.split(' '), records))
    records.sort(key=lambda x:x[1])
    current = ""
    timestamps = []
    answer = []
    for timestamp, number, in_out in records: 
        if number != current:
            if timestamps != [] and len(timestamps[-1])%2:
                timestamps[-1].append("23:59")
            current = number
            timestamps.append([])
        timestamps[-1].append(timestamp)
    
    if len(timestamps[-1])%2:
        timestamps[-1].append("23:59")
    
    for ts in timestamps:
        time = 0
        for i in range(len(ts)//2):
            time += calctime(ts[2*i], ts[2*i+1])
            
        answer.append(calc(fees, time))
    
    return answer