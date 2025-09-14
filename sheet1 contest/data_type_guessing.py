n, k, a = map(int, input().split())

# Calculate n * k / a
result = n * k / a

# Check if the result is a floating-point number
if result != int(result):
    print("double")
else:
    # Convert to integer to check range
    result_int = int(result)
    
    # Check if it fits in int range
    if -2147483648 <= result_int <= 2147483647:
        print("int")
    else:
        print("long long")