a, b = map(int, input().split())
c, d = map(int, input().split())
r = 1
t1 = b
t2 = d
while t2 != 0:
    r = t1 % t2
    t1 = t2
    t2 = r
s = (b * d) // t1
a *= (s//b)
c *= (s//d)
t1 = s
t2 = a+c
r = 1
while t2 != 0:
    r = t1 % t2
    t1 = t2
    t2 = r
ja = (a+c) // t1
mo = s // t1
print(ja, mo)