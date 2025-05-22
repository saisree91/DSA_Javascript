def peak(arr):
  n = len(arr)
  if n == 0:
      return "Array is empty"
  else:
    left = 0
    right = n - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return left 

arr = [2,3]
print(peak(arr))