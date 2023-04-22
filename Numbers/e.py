from factorial import factorial
def e():
    """Returns the value of e"""
    a = 0
    for i in range(n):
        a += 1/factorial(i)
    
    return a

def exponential(n):
    """Returns the exponential of n"""

    a = 0
    for i in range(n):
        a += n/factorial(n)
    return a