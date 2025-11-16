




def find_platform(arrival_time, departure_time):
    max_platforms = 0 
    n = len(arrival_time)
    for i in range(n):
        platforms_needed = 1 
        for j in range(n):
            if i == j:
                continue 

            
            if arrival_time[j] <= arrival_time[i] and departure_time[j] > arrival_time[i]:
                platforms_needed += 1 
        
        max_platforms = max(max_platforms, platforms_needed)
    return max_platforms 


arrival_time =  [900, 1235, 1100]
departure_time =  [1000, 1240, 1200]


result = find_platform(arrival_time, departure_time)
print(result)
