def factorial(n):
    a = 1
    for i in range(1,n+1):
        a*=i
    return a

def factorial_recursively(n):
    if n in [0,1]:
        return 1
    else:
        return factorial_recursively(n-1)