








n = int(input("Enter a target number: "))


multiple_of_2 = set()
multiple_of_3 = set()

for i in range(1, n + 1):
    multiple_of_2.add(2 * i)
    multiple_of_3.add(3 * i)


    diff  = multiple_of_2 - multiple_of_3 
    list_n = sorted(list(diff))
print(list_n)
sd = multiple_of_2.symmetric_difference(multiple_of_3)
sd = sorted(list(sd))
print(sd)


