def trappedwater(arr):
    n = len(water)
    
    # no water will be trapped if there are less than 3 element in the array
    if n <= 2:
        return 0
    
    # create two array left and right max of same length 
    left_max = [0]*n
    right_max = [0]*n
    
    # max height of the bar left of each position
    left_max[0]= arr[0]
    for i in range(1,n):
        left_max[i] = max(left_max[i-1],arr[i])
        
    # max height at the right of each position
    right_max[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], arr[i])
        
    # create a varibale to store total trapped water
    trapped_water = 0 
    
    # Iterate both array using the formula calculated for the trapped water
    
    for i in range(n):
        trapped_water = trapped_water+ max(0,min(left_max[i],right_max[i]) - arr[i])

    return trapped_water

water = [0,1,0,2,1,0,7,8,5,1,2,1]
print(trappedwater(water))