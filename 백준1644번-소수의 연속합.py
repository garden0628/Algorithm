from collections import deque
import sys
read = sys.stdin.readline

n = int(read())
sieve = [True]*(n+1)
    
for j in range(2, int(n**(1/2))+1):
    if sieve[j] == True:
        for i in range(j+j, n+1, j):
            sieve[i] = False
prime = [i for i in range(2, n+1) if sieve[i]==True]
prime.reverse()
#print(prime)

answer = 0
sum = 0
index = deque()

for k in range(len(prime)):
    sum += prime[k]
    index.append(k)
    
    if(sum == n):
        answer += 1
    elif(sum > n):
        temp = index.popleft()
        sum -= prime[temp]
        
print(answer)