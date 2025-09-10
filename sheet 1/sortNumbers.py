arr=list(map(int,input().strip().split()))
arr1=arr.copy()
arr1.sort()

for i in range(3):
    print(arr1[i])
    
print()

for i in range(3):
    print(arr[i])

