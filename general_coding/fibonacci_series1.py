def fib_series(a):
    fib_list = [0,1]
    for i in range(a-2):  # because 2 numbers already exist
      fib_list.append(fib_list[-1]+fib_list[-2])
    return fib_list


n= 5
print(fib_series(n))

