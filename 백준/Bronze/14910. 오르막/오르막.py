li = list(map(int,input().split()))
if li == sorted(li):
    print("Good")
else:
    print("Bad")