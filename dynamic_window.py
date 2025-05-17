def result(arr, k, l, r):
    sum = 0
    maxsum = 0
    length = 0
    n = len(arr)
    
    while r < n-1:
        sum += arr[r]
        while sum > k:
            sum -= arr[l]
            length -= 1
            l += 1
        if sum <= k:
          maxsum = max(maxsum, sum)
          length += 1
        r += 1
    for i in range(l, r):
        print(arr[i])
    return maxsum, length
k = 14
arr = [2,5,1,7,10]
l = r = 0
print(result(arr, k, l , r))

# TC: O(2n)
# SC: O(1)