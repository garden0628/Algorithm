formula = list(input())

answer = ""
stack = []
for i in range(len(formula)):
    if formula[i] == "(":
        stack.append(formula[i])
    elif formula[i] == "+" or formula[i] == '-':
        while stack and stack[-1] != "(":
            answer += stack.pop()
        stack.append(formula[i])
    elif formula[i] == "*" or formula[i] == "/":
        while stack and stack[-1] != "(" and (stack[-1] == "*" or stack[-1] == "/"):
            answer += stack.pop()
        stack.append(formula[i])
    elif formula[i] == ")":
        while stack and stack[-1] != "(":
            answer += stack.pop()
        stack.pop()
    else:
        answer += formula[i]

while stack:
    answer += stack.pop()

print(answer)
