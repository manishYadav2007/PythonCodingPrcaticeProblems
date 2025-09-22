


def at_least_k_occurance(arr, k):
    dict_result = {}
    for i in arr:
        dict_result[i] = dict_result.get(i, 0) + 1  
        
        if dict_result[i] == k:
            return i
    return -1





arr  = [1, 7, 4, 3, 4, 8, 7]
k = 2 


result = at_least_k_occurance(arr, k)
print(result)








# def get_majorith_element(arr):
#     majority_threshold = len(arr) / 2
#     count_element = {}
#     for i in arr:
#         count_element[i] = count_element.get(i, 0) + 1

#     for num, count in count_element.items():
#         if count > majority_threshold:
#             return num 
#     return -1 



# # arr =  [1, 1, 2, 1, 3, 5, 1]; 
# arr =  [2, 13]; 

# result = get_majorith_element(arr)
# print(result)

# class Solution:
#     def majorityElement(self, arr):
#         #code here
#         majorityElementThreshold = len(arr) / 2
#         count_element = {} 
#         for each_num in arr:
#             count_element[each_num] = count_element.get(each_num, 0) + 1

#         for num, count in count_element.items():
#             if count > majorityElementThreshold:
#                 return num 
#         return -1 
        




# arr = list(map(int, input().split()))
# obj = Solution()
# print(obj.majorityElement(arr))












# class Solution:
#     def majorityElement(self, arr):
#         majorityElements = len(arr) / 2 
#         count_element = {}
#         for i in arr:
#             count_element[i] = count_element.get(i, 0) + 1 
        
        
#         for key, value in count_element.items():
#             if value > majorityElements:
#                 return key 
#         return -1
     






# arr = list(map(int, input().split()))
# obj = Solution()
# print(obj.majorityElement(arr))





