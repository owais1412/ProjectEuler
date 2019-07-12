for a in range(1000):
    for b in range(1000):
        s = a**2 + b**2
        for c in range(1,1000):
            if (c**2 == s) and ((a+b+c)==1000):
                print (a*b*c)
                break


                
