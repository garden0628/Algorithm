import sys
import itertools
read = sys.stdin.readline

l, c = map(int, read().split())
ch = list(read().split())

ch.sort()
result = list(itertools.combinations(ch, l))
#print(result[0][0])
for i in range(len(result)):
    vowels = 0
    consonants = 0
    word = ''
    for j in range(l):
        word += result[i][j]
        if(result[i][j]=='a' or result[i][j]=='e' or result[i][j]=='i' or result[i][j]=='o' or result[i][j]=='u'):
            vowels += 1
        else:
            consonants += 1
    if(vowels>=1 and consonants>=2):
        print(word)