

def get_con_sum_list(list_num):
    con_sum_list = []
    end_index = len(list_num) - 1

    for each_index in range(end_index):
        con_sum_list.append(list_num[each_index] + list_num[each_index + 1])
    return con_sum_list


def con_sum(list_num):
    """
    The function `con_sum` iteratively calculates the consecutive sum of elements in a list until only
    one element remains.
    
    :param list_num: It looks like the code snippet you provided is a function named `con_sum` that
    takes a list of numbers as input and repeatedly calls a function `get_con_sum_list` on the list
    until there is only one element left. The function then prints the intermediate lists during this
    process
    """
    while len(list_num) > 1:
        con_sum_list  = get_con_sum_list(list_num)
        print(con_sum_list)
        list_num = con_sum_list 





list_num = list(map(int, input("Enter the list of numbers: ").split()))
print(list_num)
con_sum(list_num)