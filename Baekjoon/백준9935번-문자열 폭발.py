input_str = input()
bomb = input()

remain = []
for i in range(len(input_str)):
    remain.append(input_str[i])
    if len(remain) >= len(bomb):
        check = ''.join(remain[-len(bomb):])
        if check == bomb:
            for _ in range(len(bomb)):
                remain.pop()

answer = ''.join(remain)
if len(remain) == 0:
    answer = "FRULA"
print(answer)
