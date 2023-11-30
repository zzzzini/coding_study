a, b, c, d = map(int,input().split())
people = list(map(int,input().split()))
attack = []
for i in range(0,len(people),1):
    atck = 0
    if 0 < people[i] % (a+b) <= a:
        atck += 1
    if 0 < people[i] % (c+d) <= c:
        atck += 1
    attack.append(atck)
for item in attack:
    print(item)