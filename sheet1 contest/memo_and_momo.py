a,b,k=map(int,input().split())

if a % k==0 and b % k != 0:
    print("Memo")

elif a%k!=0 and b%k==0:
    print("Momo")

elif a%k==0 and b%k==0:
    print("Both")

else:
    print("No One")