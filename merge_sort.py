def merge(arr, low, mid, high):
    n1 = mid-low+1
    n2=high-mid
    left_arr = [0] * n1
    right_arr = [0] * n2
    for i in range(n1):
        left_arr[i] = arr[low+i]
    for j in range(n2):
        right_arr[j] = arr[mid+1+j]
    i = j = 0
    k = low
    while i<n1 and j<n2:
        if left_arr[i]<=right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    while i<n1:
        arr[k] = left_arr[i]
        i += 1
        k += 1
    while j<n2:
        arr[k] = right_arr[j]
        j += 1
        k += 1
  

def merge_sort(arr, low, high):
  
    if low < high:
        mid = (low + high)//2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid+1, high)
        merge(arr, low, mid, high)
    
# arr = [5,3,2,1]
arr = [3,1,2,4,1,5,2,6,4]
merge_sort(arr, 0, len(arr)-1)
print(arr)