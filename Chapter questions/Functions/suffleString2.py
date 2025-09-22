




def get_shuffle_string(string_input, index_list):
    suffle_str = ""
    
    for each_index in index_list:
        suffle_str += string_input[each_index]
    return suffle_str 



string_input = input("Enter the shuffle string: ")
index_list = list(map(int, input("Enter the shuffle Index: ").split())) 



result = get_shuffle_string(string_input, index_list)
print(result)


