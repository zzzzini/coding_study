import sys
text = sys.stdin.read()
alp = "abcdefghijklmnopqrstuvwxyz"
af = []
for i in alp:
  af.append(text.count(i))
mode = max(af)
position = []

ans = ""
for _ in range(af.count(mode)):
  ans += alp[af.index(mode)]
  af[af.index(mode)] = -1

print(ans)