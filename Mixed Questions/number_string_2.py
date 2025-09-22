sentence = input()

total_sum = 0 
count_of_numbers = 0 
current_num_str = ""

for char in sentence + " ":
    if char.isdigit():
        current_num_str += char 
    elif current_num_str:
        total_sum += int(current_num_str)
        count_of_numbers += 1 
        current_num_str = ""
print(total_sum)


if count_of_numbers > 0:
    avg_sum = total_sum / count_of_numbers 
    print(round(avg_sum, 2))
else:
    print(0.0)
