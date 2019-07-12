n = 100
sum_upto_n = n*(n+1)/2
sqr_upto_n = sum_upto_n**2

sqr_sum = n*(n+1)*(2*n+1)/6

print(abs(sqr_sum - sqr_upto_n))
