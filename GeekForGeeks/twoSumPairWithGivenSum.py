





def find_two_sum_pair(arr, target):
    last_index = len(arr) - 1
    unique_pairs = set()

    for cur_index in range(last_index):
        num1  = arr[cur_index]
        num2 = target - num1 
        remaining_list = arr[cur_index + 1:]

        if num2 in remaining_list:
            pairs = (num1, num2)
            unique_pairs.add(pairs)
            print(unique_pairs)
        if unique_pairs:
            return True 
    return False 








arr = list(map(int, input("Enter the list items: ").split()))
target = int(input("Enter the target value: "))


result = find_two_sum_pair(arr, target)
print(result)
