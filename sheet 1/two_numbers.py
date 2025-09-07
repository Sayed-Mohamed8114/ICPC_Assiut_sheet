from math import ceil,floor
a,b=map(int,input().split())
result=a / b
print(f"floor {a} / {b} = {floor(result)}")
print(f"ceil {a} / {b} = {ceil(result)}")

if result - int(result)==0.5:
    rounded=int(result)+1
else:
    rounded=round(result)
print(f"round {a} / {b} = {rounded}")
   