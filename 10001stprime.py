def is_prime(n):
    if n <= 1 or (n%2==0):
        return False
    if n == 2:
        return True
    counter = 3
    while ((counter*counter)<=n):
        if(n%counter==0):
            return False
        else:
            counter += 2

    return True

numPrimes = 1
n = 1
while(numPrimes<10001):
    n = n + 2
    if(is_prime(n)):
        numPrimes += 1

print(n)
