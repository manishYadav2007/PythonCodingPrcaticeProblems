base = int(input("Enter the base: "))
end_term = int(input("Enter the end term: "))

sum_of_powers = 0

power = 1 

for _ in range(end_term):
    term = base ** power
    sum_of_powers += term
    power += 2  
print(sum_of_powers)
