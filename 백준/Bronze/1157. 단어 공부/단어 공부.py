word = list(input().lower())
unique = set(word)
u_dict = {}

for item in unique:
    u_dict[item] = word.count(item)

li = [k for k, v in u_dict.items() if v == max(u_dict.values())]

if len(li) > 1:
    print("?")
else:
    print(li[0].upper())
