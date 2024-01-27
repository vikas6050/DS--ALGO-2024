def mountain(arr):
    n= len(arr)
    largest =0
    
    for i in range(1, n-2): 
        # when adjacent numbers are  decreasing we are at peak and will check forward and backward.
        if(arr[i]>arr[i-1] and arr[i]> arr[i+1]): # check if the arr[i] is at peak.
            count =1
            j=i 
            # in this we will check backward untill numbers are starts increasing.
            while(j>=1 and arr[j]>arr[j-1]):
                j -= 1
                count +=1
            # in this condition we will check in the forward direction.
            while( i <=n-2 and arr[i]>arr[i+1]):
                i += 1
                count += 1
                largest = max(largest, count)
                
        else:
            i =+1
    return largest

arr = [ 5,6,1,2,3,4,5,4,3,2,0,1,2,3,-2,4]
print(mountain(arr))