n = list(map(int, input("Enter the value: ").split()))


max_value = max(n)

first_n_num_set = set(range(1, max_value + 1))

num_set = set(n)


missing_num = first_n_num_set - num_set 

missing_num_list = list(missing_num)

missing_num_list.sort()

print(missing_num_list)



