''' In this implementation a stack to keep track of the parentheses as it
iterate through the input string. Whenever it encounter an opening parenthesis, 
it push it onto the stack. Whenever it encounter a closing parenthesis, it
pop the last opening parenthesis from the stack (if there is one) and check that
it matches the closing parenthesis. If the stack is empty at the end, the 
parentheses are balanced; otherwise, they are not. '''

def is_balanced(s: str) -> bool:
    stack = []
    for char in s:
        if char in "({[":
            stack.append(char)
        else:
            if not stack:
                return False
            if char == ")" and stack[-1] == "(":
                stack.pop()
            elif char == "}" and stack[-1] == "{":
                stack.pop()
            if char == "]" and stack[-1] == "[":
                stack.pop()
            else: 
                return False
    return not stack




