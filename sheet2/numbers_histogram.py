symbol=input()
limit=int(input())
list1=list(map(int,input().split()))
for i in range(limit):
    line=""
    line=list1[i] * symbol
    print(line)
