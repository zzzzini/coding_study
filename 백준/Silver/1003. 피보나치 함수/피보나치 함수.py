t = int(input())

z = [1,0,1]
o = [0,1,1]
def fibonacci(n):
    if len(z) <= n:
        for i in range(len(z), n+1, 1):
            z.append(z[i-1]+z[i-2])
            o.append(o[i-1]+o[i-2])
    print(z[n], o[n])

for i in range(0,t,1):
    n = int(input())
    fibonacci(n)