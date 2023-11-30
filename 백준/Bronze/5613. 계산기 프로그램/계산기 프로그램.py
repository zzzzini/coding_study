sum = int(input())
while True:
    s = input()
    if s == "=":
        break
    elif s == "+":
        n = int(input())
        sum += n
    elif s == "-":
        n = int(input())
        sum -= n
    elif s == "*":
        n = int(input())
        sum *= n
    elif s == "/":
        n = int(input())
        sum = sum // n
print(sum)