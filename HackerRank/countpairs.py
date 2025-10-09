
list_num = [0]
target_num = 100

count_pairs = 0 

len_of_list = len(list_num)


if len(list_num) <= 0:
    print(0) 


for i in range(len_of_list):
    for j in range(i + 1, len_of_list):
        if i < j and list_num[i] + list_num[j] <= target_num:
            count_pairs += 1

print(count_pairs)










