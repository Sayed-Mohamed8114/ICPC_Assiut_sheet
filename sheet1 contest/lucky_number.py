n=int(input())
list1=[]
while n>0:
    digit=n%10
    list1.append(digit)
    n//=10
if list1[0] % list1[1] == 0 or list1[1] % list1[0] == 0:
    print("YES")
else:
    print("NO") 