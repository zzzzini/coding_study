n = int(input())
w = ['kg', 'lb']
v = ['l', 'g']
dict = {
    'kg':2.2046,
    'lb':0.4536,
    'l':0.2642,
    'g':3.7854
}
for i in range(n):
    a, b = input().split()
    a = float(a)
    idx = ''
    if b in w:
        idx = w[len(w)-(w.index(b)+1)]
    else:
        idx = v[len(v)-(v.index(b)+1)]
    print('%.4f' %(a*dict[b]), idx)