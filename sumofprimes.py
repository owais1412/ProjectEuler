def isPrime(n):
    if n<=1:
        return False
    if n == 2:
        return True
    if n%2==0:
        return False
    count = 3
    while(count*count <= n):
        if(n%count==0):
            return False
        else:
            count += 2
    return True

s = 0
limit = int(2e6)
for i in range(1,limit):
    if isPrime(i):
        s += i

print(s)
