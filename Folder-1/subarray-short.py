''' 
def sorted_array(arr):
    arr1 = sorted(arr)
    n = len(arr)

    i = 0 # increase the poiner forward and check with sorted array.
    while i < n and arr[i] == arr1[i]:
        i += 1

    j = n - 1 # decrease the pointer and check with the sorted array.
    while j >= 0 and arr[j] == arr1[j]:
        j -= 1

    if i < j:
        # return arr[i:j+1]  # return unsorted array
        return [i,j] # return index of unsorted array
    else:
        return "Array is already sorted"

arr = [1, 2, 3, 4, 7, 5, 6, 8, 9, 10]
print(sorted_array(arr))
'''

# Second solution sub array sort

def subarray_sort(arr):
    n = len(arr)

    # Find the left index (i)
    i = 0
    while i < n - 1 and arr[i] <= arr[i + 1]:
        i += 1
        # print(i)
    # print(i)
    # If the array is already sorted, return a message or handle the case as needed
    if i == n - 1:
        return "Array is already sorted"

    # Find the right index (j)
    j = n - 1
    while j > 0 and arr[j] >= arr[j - 1]:
        j -= 1
    # print(j)
    # Find the minimum and maximum values in the unsorted subarray
    min_val = min(arr[i:j+1])
    max_val = max(arr[i:j+1])
    # print("min_val",min_val)
    # print("max-value", max_val)
    # Expand the subarray to include elements that are out of order
    while i > 0 and min_val < arr[i - 1]:
        i -= 1
    # print(i)
    while j < n - 1 and max_val > arr[j + 1]:
        j += 1

    return i,j  # Return the unsorted subarray

arr = [1, 2, 4, 5, 3, 7, 6, 8, 10, 12]
print(subarray_sort(arr))


        
        
            