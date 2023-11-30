shape = input()
tall = 10
for i in range(1, len(shape), 1):
    if shape[i] != shape[i-1]:
        tall += 10
    elif shape[i] == shape[i-1]:
        tall += 5
print(tall)