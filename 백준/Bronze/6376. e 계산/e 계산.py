print("n e")
print("- -----------")
for i in range(0,10,1):
    sum = 0
    adv = 1
    for j in range(0,i+1,1):
        if j == 0:
            sum = 1
        else:
            adv *= j
            sum += 1 / adv
    if i == 0 or i == 1:
        print(i, f'{sum:.0f}')
    elif i == 2:
        print(i, f'{sum:.1f}')
    else:
        print(i, f'{sum:.9f}')