def isValid(s):
    stack = []
    for i in s:
        if (i == ")" or i == "}" or i == "]") and len(stack) == 0:
            return False
        elif i == ")" and stack[-1] == "(":
            stack.pop()
        elif i == "}" and stack[-1] == "{":
            stack.pop()
        elif i == "]" and stack[-1] == "[":
            stack.pop()
        else:
            stack.append(i)
    if len(stack) > 0:
        return False
    else:
        return True
p="(())"
print(isValid(p))
