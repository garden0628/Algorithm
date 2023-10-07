n = int(input())

arr = [-1]*(n+1)
arr[1] = 0
num = 1
while(num<n):
    if(num+1<=n and (arr[num+1]==-1 or arr[num]+1<arr[num+1])):
        arr[num+1] = arr[num]+1 
    if(num*2<=n and (arr[num*2]==-1 or arr[num]+1<arr[num*2])):
        arr[num*2] = arr[num]+1   
    if(num*3<=n and (arr[num*3]==-1 or arr[num]+1<arr[num*3])):
        arr[num*3] = arr[num]+1
    
    num+=1    

print(arr[n])