s = input()
zero_idx = [k for k, v in enumerate(s) if v == '0']
one_idx = [k for k, v in enumerate(s) if v == '1']

if len(zero_idx) == 0 or len(one_idx) == 0:
    print(0)
else:
    cnt_zero = 1
    cnt_one = 1
    for i in range(1, len(zero_idx)):
        if zero_idx[i] - zero_idx[i-1] != 1:
            cnt_zero += 1

    for i in range(1, len(one_idx)):
        if one_idx[i] - one_idx[i-1] != 1:
            cnt_one += 1

    print(min(cnt_zero, cnt_one))