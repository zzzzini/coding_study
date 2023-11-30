num = int(input())
no = 1
t = 1
while True:
    if num <= no:
        print(t)
        break
    no = no + 6*t
    t = t + 1