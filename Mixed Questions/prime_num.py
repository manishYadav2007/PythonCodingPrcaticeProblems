start_num =  int(input("Enter the start number: "))
end_num = int(input("Enter the end number: "))


for i in range(start_num, end_num + 1):
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            print(i, end=" ")
                     

