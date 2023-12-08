def is_balanced(expression):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()

    return len(stack) == 0

expression1 = '([]{})'
expression2 = '([)]'
print(is_balanced(expression1))
print(is_balanced(expression2))