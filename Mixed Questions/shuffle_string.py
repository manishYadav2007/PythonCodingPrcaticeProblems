string = input("Enter the string: ") # tonyPh
suffle_index = list(map(int, input("Enter the suffle string: ").split())) # 4 3 0 5 1 2

result = ""

len_of_string = len(string) # 6

for i in range(len_of_string): # 0 1 2 3 4 5
    # first iteration i is = 0
    # second iteration i is = 1
    # second iteration i is = 2
    # second iteration i is = 3
    # second iteration i is = 4
    # second iteration i is = 5
    result += string[suffle_index[i]]
    # result = result string[suffle_index[0]] = 4 refer to = P 
    # result = result string[suffle_index[1]] = 3 refre to = y 
    # result = result string[suffle_index[2]] = 0 refre to = t  
    # result = result string[suffle_index[3]] = 5 refre to = h   
    # result = result string[suffle_index[4]] = 1 refre to = o  
    # result = result string[suffle_index[5]] = 2 refre to = n 
    
    # so the final string is Python in result   
    
