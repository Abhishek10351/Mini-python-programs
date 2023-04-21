
def find_prime_factors(num:int)->list[int]:
    """Finds the factorial for the given number"""
    prime_list = [1];
    number = int(num);
    if num%2==0:
        prime_list.append(2)
    while num%2==0:
        num = num//2;
    for i in range(3, num, 2):
        if num % i == 0:
            prime_list.append(i)
        while num % i == 0:
            num = num//i
    if len(prime_list)==0:
        prime_list.append(number)
    return prime_list
print(find_prime_factors(1680))
