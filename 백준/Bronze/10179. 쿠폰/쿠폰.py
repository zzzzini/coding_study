n = int(input())
for i in range(0,n,1):
    money = float(input())
    nm = money * 0.8
    round(nm, 2)
    print("$"+f'{nm:.2f}')