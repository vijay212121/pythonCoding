def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    rem = 0
    while x > 0:
        rem = rem * 10 + x % 10
        x = x // 10
    return rem
print(reverse(1021))