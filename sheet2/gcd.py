#get the greatest common divisor 
x,y=map(int,input().split())
gcd=[]
for i in range(1,min(x,y)+1):
    if x%i ==0 and y%i==0:
        gcd.append(i) 
print(max(gcd))