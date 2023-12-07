a, b = map(int, input().split())
if a > b:
    a, b = b, a
lefta = a % 4
leftb = b % 4

if lefta == 0:
    lefta += 4
if leftb == 0:
    leftb += 4

disc = abs(lefta - leftb)
if lefta > disc:
    newa = a - disc
else:
    newa = a + disc

disl = (b - newa) // 4

print(disc + disl)