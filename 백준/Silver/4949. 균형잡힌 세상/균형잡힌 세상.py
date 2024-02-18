while True:
    str = input()
    if str == '.':
        break
    li = [x for x in str if x in ['(','[',')',']']]
    sol = []
    flag = True

    if len(li) == 0:
        print('yes')
        continue

    if li.count('(') != li.count(')') or li.count('[') != li.count(']'):
        flag = False

    else:
        if li[0] == ')' or li[0] == ']':
            print('no')
            continue

        for item in li:
            if item == '(':
                sol.append(')')
            elif item == '[':
                sol.append(']')
            elif item == ')':
                if sol and sol[-1] == ')':
                    sol.pop()
                else:
                    flag = False
                    break
            elif item == ']':
                if sol and sol[-1] == ']':
                    sol.pop()
                else:
                    flag = False
                    break

    if flag:
        print('yes')
    else:
        print('no')