

points = [1, 2, 1, 2, 4, 7, 7, 3, 9, 4, 6, 2]


count = {}

 


for i in points:
    count[i] = count.get(i, 0) + 1

print(count)

