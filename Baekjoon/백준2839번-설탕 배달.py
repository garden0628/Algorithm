def sugar(n):
    max = int(n/5)
    answer = -1
    while (max>=0):
        if((n-(5*max))%3==0):
            answer = max + int((n-(5*max))/3)
            break
        else:
            max-=1
    
    return answer

n = int(input())
answer = sugar(n)
print(answer)