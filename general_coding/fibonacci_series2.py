def fib_range(start, end):
    a, b = 0, 1
    result = []

    while a <= end:
        if a >= start:
            result.append(a)
        a, b = b, a + b

    return result


print(fib_range(10, 50))