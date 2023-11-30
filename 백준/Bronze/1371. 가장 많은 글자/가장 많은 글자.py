import sys
text = sys.stdin.read()
alp = "abcdefghijklmnopqrstuvwxyz"
af = []
for i in alp:
  af.append(text.count(i))
mode = max(af)
position = []
for _ in range(af.count(mode)):
  position.append(af.index(mode))
  af[af.index(mode)] = -1
ans = ""
for s in position:
  ans += alp[s]
print(ans)