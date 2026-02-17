def prime_check(n):
    if n==1 or n==2:
        print("invalid numbers")
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

def first_n_primes(count):
    primes = []
    num = 2  # Start from the first prime number
    while len(primes) < count:
        if prime_check(num):
            primes.append(num)
        num += 1
    return primes
print(first_n_primes(10))