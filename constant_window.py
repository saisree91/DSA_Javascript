def const_wind(arr, l, r):
    n = len(arr)
    sum = 0
    for i in range(l,r+1):
            sum += arr[i]
    maxsum = sum
    while(r < n-1):
        sum -= arr[l]
        l += 1
        r += 1
        sum += arr[r]
        maxsum = max(maxsum, sum)
        print(l,r)
    return maxsum    
    
window_size = int(input("Enter window size"))
arr = [-1,2,3,3,4,5,-1]
l = 0
r = window_size-1
print(const_wind(arr, l, r))