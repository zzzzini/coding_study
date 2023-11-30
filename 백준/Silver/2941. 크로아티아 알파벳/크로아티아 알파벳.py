s = input()
l = 0
for i in range(1, len(s)):
    if s[i] in ['=', '-']:
        if i >= 2:
            if s[i - 2:i] == 'dz': l += 1
        l += 1

    if s[i] == 'j':
        if s[i - 1] in ['l', 'n']: l += 1
print(len(s) - l)