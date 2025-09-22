


def kSumPairs(list_input, k):
    stop_index = len(list_input) - 1
    unique_pairs = set()
    for cur_index in range(stop_index):
        num1 = list_input[cur_index]
        num2 = k - num1 
        remaining_items = list_input[cur_index + 1:]

        if num2 in remaining_items:
            pairs = (num1, num2)
            sorted_tuple = tuple(sorted(pairs))
            unique_pairs.add(sorted_tuple)
    return unique_pairs 

    



list_input = list(map(int, input("Enter the list input: ").split()))
k = int(input("Enter the k value: "))

result = kSumPairs(list_input, k)
print(result)