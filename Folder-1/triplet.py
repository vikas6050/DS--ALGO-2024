def triplet( array, target_value):
    result = []
    array.sort()
    for i in range(len(array)-2):
        j = i+1
        k = len(array)-1
        
        while (j<k):
            current_sum = array[i] +array[j] +array[k]
    
            if (current_sum == target_value):
                result.append([array[i],array[j],array[k]])
                j +=1
                k -=1
            elif (current_sum < target_value):
                j += 1
            else:
                k -=1
    return result

array = [1,2,3,4,5,6,7,8]
target_value =12
print(triplet(array,target_value))