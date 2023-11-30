alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
n = int(input())
for i in range(0,n,1):
    s1 = input().upper()
    s2 = input().upper()
    news = []
    for j in range(0,len(s1),1):
        for k in range(0,len(alphabet),1):
            if s1[j] == alphabet[k]:
                news.append(s2[k])
        if s1[j] == " ":
            news.append(" ")
    for item in news:
        print(item, end='')
    print()