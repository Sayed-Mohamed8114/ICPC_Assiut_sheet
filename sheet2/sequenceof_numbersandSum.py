while True:
    num1,num2=map(int,input().split())

    if num1 <=0 or num2 <=0: break
     
    #swap if num2 bigger than num1
    if num2 > num1: num1, num2 = num2, num1 

    
    sum=0
    while num2 <= num1:
        print(num2,end=" ")
        sum+=num2
        num2+=1
    print(f"sum ={sum}")