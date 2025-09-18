password=1999
while True:
    new_password=int(input())
    if new_password==password:
        print("Correct")
        break
    else:
        print("Wrong")
    