N = input().strip()

if "." in N:  # has decimal point
    int_part, dec_part = N.split(".")
    if int(dec_part) == 0:  # decimal part is all zeros
        print("int", int(int_part))
    else:
        print("float", int(int_part), "0." + dec_part)
              
else:  # pure integer
    print("int", int(N))