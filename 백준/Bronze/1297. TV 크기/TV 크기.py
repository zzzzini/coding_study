import math

d, h, w = map(int,(input().split()))
a = math.sqrt(d**2/(h**2 + w**2))
print(int(h*a), int(w*a))