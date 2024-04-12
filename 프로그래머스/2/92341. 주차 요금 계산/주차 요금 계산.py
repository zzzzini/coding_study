def solution(fees, records):
    answer = []
    indict = {}
    outdict = {}

    for item in records:
        time, no, state = item.split()
        hour, minute = map(int, time.split(":"))
        if state == "IN":
            indict[no] = hour * 60 + minute
        else:
            if no in outdict.keys():
                outdict[no] += (hour * 60 + minute) - indict[no]
            else:
                outdict[no] = (hour * 60 + minute) - indict[no]
            del indict[no]

    for item in indict.keys():
        if item in outdict.keys():
            outdict[item] += 1439 - indict[item]
        else:
            outdict[item] = 1439 - indict[item]


    faredict = dict(sorted(outdict.items()))
    for k, v in faredict.items():
        if v <= fees[0]:
            answer.append(fees[1])
        else:
            if (v-fees[0])%fees[2] != 0:
                answer.append(fees[1] + ((v-fees[0])//fees[2]+1)*fees[3])
            else:
                answer.append(fees[1] + ((v-fees[0])//fees[2]) * fees[3])
    return answer