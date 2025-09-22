


n = list(map(int, input("Enter the median dataset: ").split()))
n.sort()
print(n)

length = len(n)

if length % 2 == 0:
    m1 = n[length//2]
    m2 = n[length//2 - 1]
    median = (m1 + m2) / 2
else:
    median = n[length//2]

print(median)
