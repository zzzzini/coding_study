m, s = map(int,input().split())
plus = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
i = 1
days = 0
for i in range(0, m-1, 1):
    days += plus[i]
days += s
left = days % 7
d = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
print(d[left])