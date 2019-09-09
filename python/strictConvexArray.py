# Python3 program to find  minnimum in strict convex array
# minimum element 
def findMinimum(arr, low, high): 
    min = arr[low]
    for i in range(high+1): 
        if arr[i] < min: 
            min = arr[i] 
    return min

# arr = [7, 5, 3, -1, -7, 5, 9, 100] #Solution is -7
# arr = [7, 5, 3, -1, -7] #Solution is -7
arr = [-7, 5, 9, 100] #Solution is -7
# arr = [-7] #Solution is -7
n = len(arr) 
print('List is: ',arr)
print ("The minimum element is %d"% 
        findMinimum(arr, 0, n-1)) 