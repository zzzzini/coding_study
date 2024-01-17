while True:
    try:
        n, k = map(int, input().split())
        coupon = n
        temp = coupon // k
        n += temp
        coupon = temp + coupon % k
        while True:
            if coupon // k == 0:
                break
            n += coupon // k
            coupon = coupon // k + coupon % k
        print(n)
    except:
        break