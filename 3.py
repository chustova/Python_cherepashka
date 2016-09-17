n = 2
def fac(n):
    if n == 0:
        return 1
    else:
        return n*fac(n-1)
def unfac(k):
    o = k
    m = 2
    while o > 1:
        o = o/m
        p = m
        m = m + 1
    print(p)
while 1:
    r = fac(n)
    n = n + 1
    unfac(r)



