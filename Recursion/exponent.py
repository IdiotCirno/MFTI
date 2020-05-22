def exponent(x, n):
    if n%2:
        return exponent(x, n-1) * x
    elif n==2:
        return x*x
    x = exponent(x, n/2)
    return  x*x

print(exponent(2, 5))
