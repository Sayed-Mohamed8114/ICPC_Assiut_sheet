from math import sqrt
def primes(num):
    if num <2 : return False
    if num ==2 : return True
    if num %2==0 : return False
    

    limit=int(sqrt(num))
    for i in range(3,limit+1,2): 
        if num % i ==0 : return False
    return True

num=int(input())
for i in range(2,num+1):
    if primes(i): print(i,end=" ")


