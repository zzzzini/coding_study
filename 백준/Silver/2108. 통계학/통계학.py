import sys
input = sys.stdin.readline

dict = {}

n = int(input())
for i in range(n):
    num = int(input())
    if num not in dict:
        dict[num] = 1
    else:
        dict[num] += 1
v_list = [k*v for k,v in dict.items() if v != 0]
hap = sum(v_list)
avg = hap / n
if avg - (hap // n) < 0.5:
    print(hap // n)
else:
    print((hap // n) + 1)

cnt = 0
key_list = [k for k,v in dict.items() if v != 0]
key_list.sort()
t = 0
while True:
    cnt += dict[key_list[t]]
    if cnt >= (n+1)//2:
        print(key_list[t])
        break
    else:
        t += 1

m_list = [k for k,v in dict.items() if max(dict.values()) == v]
m_list.sort()
if len(m_list) > 1:
    print(m_list[1])
else:
    print(m_list[0])

print(max(key_list) - min(key_list))