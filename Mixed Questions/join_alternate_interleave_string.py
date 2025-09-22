str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")


min_len = min(len(str1), len(str2))

interleave_str = []
for i in range(min_len):
    interleave_str.append(str1[i])
    interleave_str.append(str2[i])
    
interleave_str.append(str1[min_len:])
interleave_str.append(str2[min_len:])

result  = "".join(interleave_str)
print(result)






