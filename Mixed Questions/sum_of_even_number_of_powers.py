n = int(input("Enter the base: "))
end_term = int(input("Enter the end term: "))

sum_of_terms = 0

power = 2 


for _ in range(end_term):
    terms = n ** power
    sum_of_terms += terms 
    power += 2 
print(sum_of_terms)
