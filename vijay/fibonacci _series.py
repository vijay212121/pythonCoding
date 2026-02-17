def fib_series(n):
    fib_list = [0,1]
    for i in range(n):
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list


print(fib_series(10))