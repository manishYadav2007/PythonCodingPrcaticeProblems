import math

m = int(input("Enter your first number: "))
n = int(input("Enter your second number: "))

# Find the smallest integer whose square might be in the range.
# We take the square root of m and round it up.
start_root = math.ceil(m**0.5)

# Calculate the first perfect square from that root.
first_square = start_root * start_root

if first_square <= n:
    # If this first square is within our range, we've found our answer.
    print(int(first_square))
else:
    # Otherwise, no perfect square exists in the given range.
    print("No Perfect Square")