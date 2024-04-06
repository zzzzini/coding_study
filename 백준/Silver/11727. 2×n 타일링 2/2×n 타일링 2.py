n = int(input())
li = [1,3]
for i in range(2,n):
    li.append((li[i-1] + 2*li[i-2])%10007)
print(li[n-1])