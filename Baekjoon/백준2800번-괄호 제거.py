import sys
from itertools import combinations
read = sys.stdin.readline

formula = read().strip()
li = []
seq = []

for i in range(len(formula)):
  if formula[i]=='(':
    li.append(i)
  elif formula[i]==')':
    seq.append([li.pop(), i])
    
answer = set()

for i in range(1, len(seq)+1):
  remove = combinations(seq, i)

  for j in remove:
    target = list(formula)
    for k in j:
      target[k[0]] = ""
      target[k[1]] = ""

    answer.add(''.join(target))


for val in sorted(list(answer)):
  print(val)
