l, p = map(int,input().split())
people = l * p
news = list(map(int,input().split()))
for i in range(0,len(news),1):
    print(news[i] - people, end=' ')