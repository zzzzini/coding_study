import math

n = int(input())
l = input()
hash = 0

alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
key = [(i+1) for i in range(26)]

count = 0
for items in l:
    hash += (key[alpha.index(items)] * math.pow(31, count))
    count += 1
print("%d" %hash)