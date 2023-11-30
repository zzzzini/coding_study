v = []
for i in range(0,3,1):
    v.append(int(input()))
cnt = 0
for i in range(0,2,1):
    for j in range(i+1,3,1):
        if v[i] == v[j]:
            cnt += 1
if v[0] == v[1] == v[2] == 60:
    print("Equilateral")
elif sum(v) == 180 and cnt >= 1:
    print("Isosceles")
elif sum(v) == 180 and cnt == 0:
    print("Scalene")
elif sum(v) != 180:
    print("Error")