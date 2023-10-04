import sys
input = sys.stdin.readline

n, k = map(int, input().split())
scores = list(map(int, input().split()))

for _ in range(k):
    start, end = map(int, input().split())
    avg = sum(scores[start-1:end])/(end-start+1)
    print("{:.2f}".format(avg))
