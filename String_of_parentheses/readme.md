Write a function that takes a string of parentheses as input, and returns 'True' 
if the parentheses are balanced and 'False' otherwise. A string of parentheses is
considered balanced if each opening parenthesis has a corresponding closing parenthesis,
and the order of the parentheses is maintained.

For example, the following strings of parentheses are balanced:

"(())"

"((()))"

"()()"

The following strings of parentheses are not balanced:

"(("

"())"

"(()"


Signature
```
def is_balanced(s: str) -> bool:
    __input__ :  a string as 's' which represents the string of Parentheses
               (0 <= len(s) <= 10^6)
    __output__: return Boolean value indicating the balance of Parentheses
    
    - This function will balance the Parentheses using stack implementation
```  

Example
```
assert is_balanced("()") == True
assert is_balanced("()[]{}") == True
assert is_balanced("(]") == False
assert is_balanced("([)]") == False
assert is_balanced("{[]}") == True
```

Note: A Parentheses could be either '()' or '{}' or '[]'
