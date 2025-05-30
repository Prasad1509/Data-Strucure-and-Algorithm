def evaluate_postfix(exp):
    stack = []
    for ch in exp:
        if ch.isdigit():
            stack.append(int(ch))
        else:
            b = stack.pop()
            a = stack.pop()
            if ch == '+':
                stack.append(a + b)
            elif ch == '*':
                stack.append(a * b)
    return stack[0]

print(evaluate_postfix("23*4+")) 
