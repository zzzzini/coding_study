month = [31,28,31,30,31,30,31,31,30,31,30,31]
day = ["Wednesday","Thursday", "Friday", "Saturday", "Sunday","Monday", "Tuesday" ]
d,m=map(int,input().split())
print(day[(sum(month[i] for i in range(m-1)) + d) % 7])