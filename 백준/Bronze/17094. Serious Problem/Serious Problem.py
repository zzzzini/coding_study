n = int(input())
c = input()
e = 0
two = 0
for i in range(0, n, 1):
    if c[i] == "2":
        two += 1
    elif c[i] == "e":
        e += 1
if two > e:
    print(2)
elif e > two:
    print("e")
elif two == e:
    print("yee")