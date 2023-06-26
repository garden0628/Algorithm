from collections import deque

T = int(input())

for _ in range(T):
    p = list(input())
    n = int(input())
    nums = deque()
    string = input().lstrip('[').rstrip(']')

    if n != 0:
        nums = deque(list(string.split(',')))

    count_r = 0
    error_flag = 0
    for func in p:
        if func == "R":
            count_r += 1
        elif func == "D":
            if len(nums) == 0:
                print("error")
                error_flag = 1
                break
            if count_r % 2 == 0:
                nums.popleft()
            else:
                nums.pop()

    if count_r % 2 == 1:
        nums = deque(list(reversed(nums)))

    if error_flag == 0:
        answer = '['
        while nums:
            answer += str(nums.popleft())
            answer += ","
        answer = answer.rstrip(',')
        answer += ']'
        print(answer)

