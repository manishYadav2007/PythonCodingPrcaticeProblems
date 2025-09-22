
str1 = "ramisgood"
str2 = "goodforall"

result  =""

length = len(str1)


for each_index in range(length):
    if str2.startswith(str1[each_index:]):
        result += str1[each_index:]
        break
else:
    result = "No overlapping"


print(result)


