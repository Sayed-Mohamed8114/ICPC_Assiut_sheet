n=int(input())
arr=list(map(int,input().split()))
even,odd,positive,negative=0,0,0,0
for num in arr:
    if num%2==0:
        even+=1
    if num %2 !=0:
        odd+=1
    if num >0:
        positive+=1
    if num <0:
        negative+=1
        
print(f"Even: {even}")
print(f"Odd: {odd}")
print(f"Positive: {positive}")
print(f"Negative: {negative}")