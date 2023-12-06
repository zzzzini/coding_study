y = (30, 10)
m = (60, 15)

n = int(input())
test = list(map(int, input().split()))

y_sum = 0
m_sum = 0

for item in test:
    y_sum += (((item//y[0])+1)*y[1])
    m_sum += (((item//m[0])+1)*m[1])

if y_sum > m_sum:
    print("M %d" %m_sum)
elif m_sum > y_sum:
    print("Y %d" %y_sum)
elif y_sum == m_sum:
    print("Y M %d" %y_sum)