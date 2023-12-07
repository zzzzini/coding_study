alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
answer = []
s = input()
for item in alpha:
    if item in s:
        answer.append(s.index(item))
        continue
    else:
        answer.append(-1)
for item in answer:
    print(item, end=' ')