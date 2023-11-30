n = int(input())
s = input()
acnt = 0
bcnt = 0
for i in range(0,n,1):
    if s[i] == "A":
        acnt += 1
    elif s[i] == "B":
        bcnt += 1
if acnt > bcnt:
    print("A")
elif acnt == bcnt:
    print("Tie")
else:
    print("B")