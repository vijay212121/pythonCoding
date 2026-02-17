"""#using recursion
def fact_num(n):
    fact = 1
    for i in range(1, n+1):
        fact = n * fact_num(n-1)
    return fact
print(fact_num(5))


"""
def fact_num(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact*i
    return fact
print(fact_num(5))
