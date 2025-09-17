n=int(input())
list1=[]
for _ in range(n):
    list1.append(int(input()))

    
for i in range(len(list1)):
    factorial=1
    while list1[i] >0:
        factorial=factorial*list1[i]
        list1[i]-=1

    print(factorial)