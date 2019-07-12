from math import ceil, floor
for i in range(1,21):
    while True:
        j = 2520
        a = floor(j/i)
        b = ceil(j/i)
        c = a-b
        if c == -1:
            j = j + 1
        else:
            continue

print(j)
