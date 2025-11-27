def isPerfect(n):
    if n == 1:
        return False
    
    s  = 1
    i = 2
    while i <= n**0.5:
        if n % i == 0:
            s += i
            
            other = n // i
            if other != i:
                s += other
        i += 1
    return s == n

n = 6
print(isPerfect(n))

