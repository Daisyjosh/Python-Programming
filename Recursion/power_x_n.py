def power(x,n):
    if n == 0:
        return 1
    halfpow = power(x,int(n/2))
    halfpowSQ = halfpow*halfpow
    if n % 2 != 0:
        return halfpowSQ*x
    else:
        return halfpowSQ
print(power(2,10))