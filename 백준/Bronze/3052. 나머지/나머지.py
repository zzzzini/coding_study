num = []
left = []
for i in range(0,10,1):
    num.append(int(input()))
    if num[i]%42 not in left:
        left.append(num[i]%42)
print(len(left))