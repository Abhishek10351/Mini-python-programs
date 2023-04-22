def fibonacci(n):
    """Returns the n-th term of Fibonacci series"""
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

def fibonacci_recursive(n):
    """Returns the n-th term of Fibonacci series using recursion"""
    if n in [0,1]:
        return 1
    else:
        return fibonacci_recursive(n-1)+n