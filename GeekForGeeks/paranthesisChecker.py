


def is_paranthesis_balanced(s):
    comb = {
        ")": "(",
        "}": "{",
        "]": "["
    }
    openings = ['(', '{', '[']
    stack = []
    length_arr  = len(s) - 1 
    i = 0 

    while i <= length_arr:
        if s[i] in openings:
            stack.append(s[i])
        else:
            if stack and stack[-1] == comb[s[i]]:
                stack.pop()
            else:
                return False 
        i += 1 
    return not len(stack)



s = "([{]})"

result = is_paranthesis_balanced(s)
print(result)