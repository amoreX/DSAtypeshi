global result
result=""
global stack
stack=[""]

def append(word):
    global result
    global stack
    result+=word
    stack.append(result)
    return result

def undo():
    global result
    global stack
    stack.pop()
    result=stack[-1]x
    return result

print(append("Hello"))
print(append(" World"))
print(undo())
print(undo())
