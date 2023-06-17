string = list(input())

answer = []
temp = ""
i = 0
while i < len(string):
    if string[i] == "<" or string[i] == ">" or string[i] == "(" or string[i] == ")":
        if len(temp) > 0:
            answer.append(temp)
            temp = ""
        answer.append(string[i])
    elif string[i] == "&" or string[i] == "|":
        if len(temp)>0:
            answer.append(temp)
            temp = ""
        answer.append(string[i]+string[i+1])
        i += 1
    elif string[i] == " ":
        if len(temp)>0:
            answer.append(temp)
            temp = ""
    else:
        temp += string[i]

    i += 1

if len(temp) > 0:
    answer.append(temp)
print(' '.join(answer))
