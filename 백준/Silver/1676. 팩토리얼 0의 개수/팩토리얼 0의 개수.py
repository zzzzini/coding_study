n = int(input())
k = 1
for i in range(1,n+1,1):
    k *= i
k = str(k)
cnt = 0
for i in range(len(k)-1, 1, -1):
    if k[i] == "0":
        cnt += 1
    else:
        break
print(cnt)