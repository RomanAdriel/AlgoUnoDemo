def fact_1(N):
    factorial_total = 1
    while N > 1:
        factorial_total *= N
        N -= 1
    return factorial_total
