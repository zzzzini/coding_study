s = input()
for i in ["a","e","i","o","u"]:
    s = s.replace(i+"p"+i,i)
print(s)