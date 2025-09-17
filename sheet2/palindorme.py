n=int(input())
string=str(n)
palindorme=string[::-1]

if int(palindorme)==n:
    print(int(palindorme))
    print("YES")
else:
    print(int(palindorme))
    print("NO")