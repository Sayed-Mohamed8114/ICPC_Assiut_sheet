from math import sqrt

def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check only odd numbers up to sqrt(n)
    limit = int(sqrt(n))
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
    return True

# Get input from user
n = int(input())

# Check if the number is prime
if is_prime(n):
    print("YES")
else:
    print("NO")