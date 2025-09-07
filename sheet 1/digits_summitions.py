nums=list(map(int,input().split()))
sum=0
for i in nums:
    digit = i %10
    sum+=digit
print(sum)