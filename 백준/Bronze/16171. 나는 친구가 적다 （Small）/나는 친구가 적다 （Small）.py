s = input()
k = input()
text = ""
for i in s:
    if not (i >= '0' and i <= '9'):
        text += i
if k in text:
    print(1)
else:
    print(0)