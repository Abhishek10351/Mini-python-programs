def is_happy(n, data=[]):
    
    """**Happy Numbers ** - A happy number is defined by the following process. Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1."""

    a = [int(i)**2 for i in str(n)]
    a = sum(a)
    
    if n == 1:
        return True
    elif n in data:
        return False

    data.append(n)
    return is_happy(a,data)
