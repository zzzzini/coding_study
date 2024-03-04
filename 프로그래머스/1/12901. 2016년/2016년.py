import datetime

def solution(a, b):
    li = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    day = datetime.date(2016,1,1)
    today = datetime.date(2016,a,b)
    diff = (today-day).days
    diff = diff % 7
    date = li.index("FRI")+diff
    if date >= 7:
        date -= 7
    answer = li[date]
    return answer