x=int(input())
evens=[]
for i in range(1,x+1):
    if i %2==0:
        evens.append(i)

if not evens:
    print(-1)
else:
    for i in range(len(evens)):
        print(evens[i])




        
