




def get_shuffle_string(string_input, index_list):
    suffle_str = ""
    length = len(string_input)
    for each_index in range(length):
        suffle_str += string_input[index_list[each_index]]
    return suffle_str 




string_input = input("Enter the shuffle string: ")
index_list = list(map(int, input("Enter the shuffle Index: ").split())) 



result = get_shuffle_string(string_input, index_list)
print(result)


