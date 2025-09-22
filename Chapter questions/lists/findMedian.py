
m = list(map(int, input("Enter the list items: ").split()))

m.sort()

len_of_list  = len(m)


if len_of_list % 2 == 0:
    m1 = m[len_of_list//2]
    m2 = m[len_of_list//2 - 1]
    median = (m1 + m2) / 2 
else:
    median = m[len_of_list //2]

print(median)





    