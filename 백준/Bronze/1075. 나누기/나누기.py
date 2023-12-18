n = int(input())
f = int(input())

k = (n // 100) * 100
if k % f == 0:
    print(str(f*(k//f))[-2::])
else:
    print(str(f*((k//f)+1))[-2::])