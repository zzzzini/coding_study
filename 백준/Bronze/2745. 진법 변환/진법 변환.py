numbers = ["-","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
n, b = input().split()
b = int(b)
sum = 0
for i in range(0,len(n),1):
    for j in range(0,len(numbers),1):
        if n[i] == numbers[j]:
            sum += j * (b ** (len(n) - (i+1)))
print(sum)