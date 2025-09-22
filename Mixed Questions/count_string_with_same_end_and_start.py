list_a = ['abc', 'xyz', 'aba', '1221']
k = 0
for i in list_a:
    if len(i) > 1 and i[0] == i[-1]:
        k += 1
print(k)


              
    