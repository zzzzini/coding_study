alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
t = int(input())
for i in range(0,t,1):
    s, n = input().split('-')
    s = s.lower()
    sum = 0
    for j in range(0,3,1):
        for k in range(0,len(alphabet),1):
            if s[j] == alphabet[k]:
                sum += k * (26 ** (2-j))
    if abs(int(n) - sum) > 100:
        print("not nice")
    else:
        print("nice")