import sys
read = sys.stdin.readline

string = read().rstrip()
m = int(read())

key = []
score = [-1 for _ in range(len(string))]

for i in range(m):
  key.append(list(map(str, read().split())))
  key[-1][1] = int(key[-1][1])

def func(index):
  global score

  if index >= len(string): return 0
  if score[index] != -1: return score[index]

  score[index] = func(index + 1) + 1
  for i in range(len(key)):
    if string[index:index+len(key[i][0])] == key[i][0]:
      score[index] = max(score[index], func(index + len(key[i][0])) + key[i][1])

  return score[index]

print(func(0))
