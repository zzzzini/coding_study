found = []
for i in range(0,5,1):
    s = input()
    if "FBI" in s:
        found.append(i+1)
if len(found) != 0:
    for i in range(0,len(found),1):
        print(found[i])
else:
    print("HE GOT AWAY!")