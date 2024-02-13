import datetime

mondict = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

m, d, y, hmin = input().split()
d = d[:2]
m = mondict[m]
h, min = hmin[:2], hmin[-2:]

dt = datetime.datetime(int(y), m, int(d), int(h), int(min))
first = datetime.datetime(int(y), 1, 1)
last = datetime.datetime(int(y)+1, 1, 1)

diff = (((last-dt).days)*24*60*60 + (last-dt).seconds) / (((last-first).days)*24*60*60)
print((1 - diff)*100)