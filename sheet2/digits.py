t = int(input())

for _ in range(t):
    n = int(input())
    
    # Handle the case where n = 0
    if n == 0:
        print("0")
        continue
    
    digits = []
    while n > 0:
        digit = n % 10
        digits.append(str(digit))
        n //= 10
    
    # Print digits separated by space
    print(" ".join(digits))
