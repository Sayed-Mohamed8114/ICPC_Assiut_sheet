# classic way of interval problems we need to get the min of the right in the two sets and the max of the left in the two sets
# then return the start and the end if start <=end else return -1

l1,r1,l2,r2=map(int,input().split())
start = max(l1, l2)
end = min(r1, r2)

if start<=end:
    print(start,end)
else:
    print(-1)