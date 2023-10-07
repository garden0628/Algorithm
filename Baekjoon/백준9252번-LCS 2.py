def findLCS(str1, str2):
    board = [[0]*(len(str1)+1) for _ in range(len(str2)+1)]
    for i in range(len(str2)):
        for j in range(len(str1)):
            if str1[j] == str2[i]:
                board[i+1][j+1] = board[i][j] + 1
            else:
                board[i+1][j+1] = max(board[i][j+1], board[i+1][j])

    string_list = []
    x, y = len(str2), len(str1)
    while board[x][y] != 0:
        if board[x][y] == board[x-1][y]:
            x -= 1
        elif board[x][y] == board[x][y-1]:
            y -= 1
        else:
            string_list.append(str2[x-1])
            x, y = x-1, y-1

    string_list.reverse()
    lcs = ''.join(string_list)

    return lcs

first = input()
second = input()

answer = findLCS(first, second)
length = len(answer)

print(length)
if length!=0: print(answer)
