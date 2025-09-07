def summation(n):
    return n * (n + 1) // 2  

n = int(input("Enter a number n: "))
print("Summation from 1 to", n, "=", summation(n))