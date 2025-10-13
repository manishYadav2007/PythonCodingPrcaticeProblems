







# --- Approach 2: Optimal - The Stack Method (O(n) Time) ---
# Yeh aapka hi code hai, thoda aur saaf-suthra likha hua.
def is_paranthesis_balanced(s):
    stack = []

    bracket_map = {")": "(", "}": "{", "]": "["}
    for i in s:
         if i in bracket_map:
              if stack and stack[-1] == bracket_map[i]:
                   stack.pop()
              else:
                   return False 
         else:
              stack.append(i)
    return not stack      

string = "([{]})"

result = is_paranthesis_balanced(string)
print(result)








