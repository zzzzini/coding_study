def sosu(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in range(0,len(alphabet),1):
    alphabet.append(alphabet[i].upper())
number = 0
s = input()
for i in range(0,len(s),1):
    for j in range(0,len(alphabet),1):
        if s[i] == alphabet[j]:
            number += j + 1
            break
if sosu(number) or number == 1:
    print("It is a prime word.")
else:
    print("It is not a prime word.")