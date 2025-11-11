



def find_armstrong_number(target_num):
    armstrong_number = 0 
    for i in target_num:
        power = int(i) ** 3 
        armstrong_number += power 
    
    if armstrong_number == int(target_num):
        return True 
    else:
        return False



target_num = input("Enter a number: ")

result = find_armstrong_number(target_num)
print(result)

