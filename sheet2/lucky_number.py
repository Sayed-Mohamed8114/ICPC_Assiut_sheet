def lucky(x,y):
    result=[]
    for num in range(x,y+1):
        if all(ch in "47" for ch in str(num)):
            result.append(str(num))
    if result:
        print(" ".join(result))
    else:
        print(-1)
x,y=map(int,input().split())
lucky(x,y)