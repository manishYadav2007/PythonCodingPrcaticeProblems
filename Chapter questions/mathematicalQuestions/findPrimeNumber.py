


def findPrimeNumber(n):
    count_factors = 0 
    for i in range(2, n):
        if (n % i) == 0:
            count_factors += 1 
    if count_factors == 0:
        return "Prime Number"
    else:
        return "Not a Prime Number"




n = 6
result = findPrimeNumber(n)
print(result)

