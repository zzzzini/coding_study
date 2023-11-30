a = input()
b = input()
print(sum(abs(a.count(c)-b.count(c))for c in{*a+b}))