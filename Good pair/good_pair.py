def good_pair(array,k):
    size=len(array)
    for i in range(size):
        for j in range(i+1,size):
            if array[i]+array[j]==k:
                return 1
    
    return 0
    
array=list(map(int,input().split()))
k=int(input())
print(good_pair(array,k))