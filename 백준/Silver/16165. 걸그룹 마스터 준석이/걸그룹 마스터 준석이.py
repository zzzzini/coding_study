n, m = map(int, input().split())
otaku = {}
for i in range(n):
    group = input()
    members = []
    for j in range(int(input())):
        members.append(input())
    otaku[group] = members

for i in range(m):
    name = input()
    type = int(input())

    if type == 0:
        for item in sorted(otaku[name]):
            print(item)
    else:
        print([k for k, v in otaku.items() if name in v][0])