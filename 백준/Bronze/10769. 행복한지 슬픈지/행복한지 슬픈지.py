s = input()
happy = 0
sad = 0
for i in range(0,len(s)-2,1):
    if s[i] == ":" and s[i+1] == "-" and s[i+2] == ")":
        happy += 1
    elif s[i] == ":" and s[i+1] == "-" and s[i+2] == "(":
        sad += 1
if happy == sad == 0:
    print("none")
elif happy > sad:
    print("happy")
elif happy < sad:
    print("sad")
elif happy == sad:
    print("unsure")