def merge(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    n3 = n1 + n2
    arr3 = [0] * n3
    i = j = k = 0
    while i < n1 and j < n2:
        if arr1[i] < arr2[j]:
            arr3[k] = arr1[i]
            i += 1
        else:
            arr3[k] = arr2[j]
            j += 1
        k += 1
    while i < n1:
        arr3[k] = arr1[i]
        i += 1
        k += 1
    while j < n2:
        arr3[k] = arr2[j]
        j += 1
        k += 1
    return arr3
        

arr1 = [4,7,9]
arr2 = [2,5,8]
print(merge(arr1, arr2))
