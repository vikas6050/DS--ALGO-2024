def largestband(arr):
    arr = set(arr) # create a set of array.
    max_length =1
    
    for num in arr:
        if num-1 not in arr: # check if num is the starting element of the band
            start_num = num
            initial_length = 1
            
            while start_num +1 in arr: # keep checking consecutive element of the band.
                start_num += 1
                initial_length += 1
                
            max_length = max (max_length, initial_length)
            
    return max_length
       
    
arr = [1,9,3,0,18,5,2,4,10,7,12,6]
print(largestband(arr))