n = int(input())
kpa = 5 * n - 400
if kpa > 100:
    i = -1
elif kpa == 100:
    i = 0
else:
    i = 1
print(kpa)
print(i)