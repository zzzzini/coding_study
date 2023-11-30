s = input()
new = []
for i in range(0,len(s),1):
    if s[i] == s[i].lower():
        new.append(s[i].upper())
    else:
        new.append(s[i].lower())
for i in range(0,len(new),1):
    print(new[i], end='')