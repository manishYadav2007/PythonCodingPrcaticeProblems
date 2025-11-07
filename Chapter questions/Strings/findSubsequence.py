
# # orignal_string = input("Enter the orignal String: ")
# # substring  = input("Enter the substring: ")

# # sub_seq_index = 0 

# # sub_seq_string_length = len(substring)


# # for each_char in orignal_string:
# #     if each_char == substring[sub_seq_index]:
# #         sub_seq_index += 1 

# #         if sub_seq_index == sub_seq_string_length:
# #             break 
    
# # if sub_seq_index == sub_seq_string_length:
# #     print("Yes! This is a subsequence of the original string")
# # else:
# #     print("No! This is not a subsequence of the original string")





















orignal_str = input("Enter the original string: ")
subsequence_str = input("Enter the subsequence string: ")

sub_seq_index = 0 

len_of_sub_seq = len(subsequence_str)



for i in orignal_str:
    if i == subsequence_str[sub_seq_index]:
        sub_seq_index +=  1
        
        if sub_seq_index == len_of_sub_seq:
            break

if sub_seq_index == len_of_sub_seq:
    print("Yes")
else:
    print("No")








































# num = 1, 2, 3

# print(num[1])






