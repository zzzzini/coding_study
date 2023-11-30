while True:
    s = input()
    if s == "EOI":
        break
    prime = s.lower()
    if prime.find("nemo") != -1:
        print("Found")
    else:
        print("Missing")