def check_pal(n):
    n = str(n)
    return n == n[::-1]


max_pal = 0
for i in range(100,1000):
    for j in range(100,1000):
        temp = i*j
        check = check_pal(temp)
        if check and (temp > max_pal):
            max_pal = temp


print(max_pal)
