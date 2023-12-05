n = int(input())
l = input()
hash = 0
mod = 1234567891
count = 0
for items in l:
    hash += ((ord(items)-96) * (31 ** count))
    count += 1
print(hash % mod)