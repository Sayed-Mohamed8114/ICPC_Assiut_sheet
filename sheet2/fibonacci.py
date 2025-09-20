# with recursion 
'''
def fib(num):
    if num ==0 or num ==1:
        return 0

    if num ==2 :
        return 1
    
    return fib(num-1) + fib(num-2)

n=int(input())
for i in range(1,n+1):
    print(fib(i),end=" ")
  '''  

# another way 
def fib(num):
    if num ==0 or num ==1:
        return 0

    if num ==2 :
        return 1
    
    a,b=0,1
    for _ in range(3, num + 1):
        a, b = b, a + b
    return b

n = int(input())
for i in range(1, n + 1):
    print(fib(i), end=" ")
