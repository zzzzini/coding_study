s = input()
for i in range(0,len(s),1):
    if s[i] == "C" or s[i] == "A" or s[i] == "M" or s[i] == "B" or s[i] == "R" or s[i] == "I" or s[i] == "D" or s[i] == "G" or s[i] == "E":
        continue
    else:
        print(s[i], end='')