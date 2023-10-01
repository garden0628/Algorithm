import sys
input = sys.stdin.readline

n = int(input())
total_score = [0]*n

def make_rank(scores):
    new_list = []
    for i in range(len(scores)):
        new_list.append([scores[i], i])
    new_list.sort(reverse=True)
    
    ranking = [0]*n
    prev_score = 1000*n+1
    rank = 0
    for i in range(len(new_list)):
        score, idx = new_list[i][0], new_list[i][1]
        if prev_score > score:
            ranking[idx] = i+1
            prev_score = score
            rank = i+1
        elif prev_score == score:
            ranking[idx] = rank
    
    return ranking


for _ in range(3):
    scores = list(map(int, input().split()))
    total_score = [total_score[i]+scores[i] for i in range(len(scores))]
    
    ranking = make_rank(scores)
    
    for rank in ranking:
        print(rank, end=" ")
    print()

# print(total_score)
ranking = make_rank(total_score)
for rank in ranking:
    print(rank, end=" ")
