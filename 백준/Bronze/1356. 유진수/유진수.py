n = input()
flag = False
for i in range(0,len(n)-1,1):
    alpha = n[0:i+1]
    beta = n[i+1:len(n)]

    m_alpha = 1
    m_beta = 1

    for item in alpha:
        m_alpha *= int(item)

    for item in beta:
        m_beta *= int(item)

    if m_alpha == m_beta:
        flag = True
        break

if flag:
    print("YES")
else:
    print("NO")