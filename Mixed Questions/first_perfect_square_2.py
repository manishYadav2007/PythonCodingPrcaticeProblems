m = int(input("Enter your first number: "))
n = int(input("Enter your second number: "))

# Start with the number 1 to find the first root.
i = 1

# Find the smallest integer 'i' whose square is greater than or equal to m.
# This loop is very fast because it only runs up to the square root of m.
while i * i < m:
    i += 1

# 'i * i' is now the first perfect square at or after m.
first_perfect_square = i * i

# Check if this first perfect square is within the allowed range [m, n].
if first_perfect_square <= n:
    print(first_perfect_square)
else:
    print("No Perfect Square")