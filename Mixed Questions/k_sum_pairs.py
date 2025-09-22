

# def get_pairs(list_items, target_value):
#     stop_index = len(list_items) - 1 
#     unique_pairs = set()
    
#     for cur_index in range(stop_index):
#         num_1 = list_items[cur_index]
#         num_2 = target_value - num_1 
#         remaining_items = list_items[cur_index + 1:]
#         if num_2 in remaining_items:
#             pairs = (num_1, num_2)
#             sorted_tuple = tuple(sorted([pairs]))
#             unique_pairs.add(sorted_tuple) 
#     return unique_pairs   







# list_items = list(map(int, input("Enter the list items: ").split(',')))
# target_value = int(input("Enter the target sum value: "))

# result = get_pairs(list_items, target_value)
# # print(result)

# result = sorted(result)

# for each_pairs in result:
#     print(each_pairs)
    







# def get_pairs(list_n, target_value):
#     # [5 3 7 9 5]
#     # 12
#     stop_index = len(list_n) - 1
#     unique_pairs = set()
#     for cur_index in range(stop_index):
#         num1 = list_n[cur_index]
#         num2 = target_value - num1 
#         remaining_list = list_n[cur_index + 1:]
        
#         if num2 in remaining_list:
#             pairs = (num1,  num2)
    
#             sorted_tuple = tuple(sorted(pairs))
#             unique_pairs.add(sorted_tuple)
#     return unique_pairs

    
        
        


# list_n = list(map(int, input("Enter the list items: ").split()))
# target_value = int(input("Enter the target value: "))

# result = get_pairs(list_n, target_value)
# print(result)
# result = sorted(result)


# for each_pair in result:
#     print(each_pair)







def get_pairs(list_items, target_value):
    # list item = [5, 3, 7, 9, 5]
    # target value = 12
    stop_index = len(list_items) - 1 
    unique_pairs = set() 
    for cur_index in range(stop_index):
        num1 = list_items[cur_index] 
        num2 = target_value - num1 
        remaining_list = list_items[cur_index + 1:]
        if num2 in remaining_list:
            pairs = (num1, num2)
            sorted_tuple = tuple(sorted(pairs))
            unique_pairs.add(sorted_tuple)
    return unique_pairs 
    

list_item = list(map(int, input("Enter the list items: ").split()))
k = int(input("Enter the k value: "))

result = get_pairs(list_item, k)

result = sorted(result)
for each_item in result:
    print(each_item) 




