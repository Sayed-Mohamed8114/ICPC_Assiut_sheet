# Read 4 numbers
A, B, C, D = map(int, input().split())

# Calculate product modulo 100
result = (A * B * C * D) % 100

# Print last 2 digits with leading zero if needed
print(f"{result:02d}")