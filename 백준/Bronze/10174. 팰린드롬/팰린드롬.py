n = int(input())
for i in range(0, n, 1):
    s = input().upper()
    if s == s[::-1]:
        print("Yes")
    else:
        print("No")