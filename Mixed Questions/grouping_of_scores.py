

# def get_scores(scores):
#     pairs = {}
#     for item in scores:
#         pair = item.split(':')
#         key, value = pair[0], int(pair[1])
        
#         if key in pairs:
#             score = pairs[key]
#             pairs[key] = score + value
#         else:
#             pairs[key] = value 
#     return pairs 
        




# scores = input("Enter the user scores: ").split()
# # print(scores)
# result = get_scores(scores)
# result = result.items()
# result = sorted(result)
# print(result)



def get_scores(ball_score_dict):
    pairs = {}
    for item in ball_score_dict:
        pair = item.split(":")
        key, value = pair[0],  int(pair[1])
        pairs[key] = value 
        if key in pairs:
            score = pairs[key]
            pairs[key] = score + value 
        else:
            pairs[key] = value 
    return pairs  




ball_score_dict = input("Enter the dictinory score: ").split() 
print(ball_score_dict)

result = get_scores(ball_score_dict)
print(result)