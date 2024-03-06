n, m = map(int, input().split())
package = []
one = []
for i in range(m):
    p, c = map(int, input().split())
    package.append(p)
    one.append(c)

print(min(((n//6)+1)*min(package), (n//6)*min(package)+(n%6)*min(one), min(one)*n))