def fib(n):
    """
    Generate Fibonacci series
    """
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()


def fib2(n): # return Fibonacci series up to n
    """
    Generate Fibonacci series as list
    """
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

if __name__ == '__main__':
    fib(10)
    print(fib2(10))