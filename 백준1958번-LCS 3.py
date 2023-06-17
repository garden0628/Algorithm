def findLCS(str1, str2, str3):
    l1, l2, l3 = len(str1), len(str2), len(str3)
    board = [[[0 for i in range(l3+1)] for j in range(l2+1)] for k in range(l1+1)]
    for i in range(1, l1+1):
        for j in range(1, l2+1):
            for k in range(1, l3+1):
                if str1[i-1] == str2[j-1] == str3[k-1]:
                    board[i][j][k] = board[i-1][j-1][k-1] + 1
                else:
                    board[i][j][k] = max(board[i-1][j][k], board[i][j-1][k], board[i][j][k-1])

    return board[l1][l2][l3]

first = input()
second = input()
third = input()

print(findLCS(first, second, third))
