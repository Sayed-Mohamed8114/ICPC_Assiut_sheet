a,b=map(float,input().split())

coordinates=["Q1","Q2","Q3","Q4"]


if a == 0 and b == 0:
    print("Origem")
elif a == 0:
    print("Eixo Y")
elif b == 0:
    print("Eixo X")
elif a>0 and b>0:
    print(coordinates[0])
elif a>0 and b<0:
    print(coordinates[3])
elif a<0 and b>0:
    print(coordinates[1])
elif a<0 and b<0:
    print(coordinates[2])
    