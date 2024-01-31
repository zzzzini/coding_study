data = {"AG":"C", "AC":"A", "AT":"G", "GC":"T", "GT":"A", "CT":"G"}

n = int(input())
dna = list(input())

last = dna.pop()

for i in range(n-1):
    first = dna.pop()

    if first == last:
        continue
    else:
        if first+last in data.keys():
            last = data[first+last]
        else:
            last = data[(first+last)[::-1]]

print(last)