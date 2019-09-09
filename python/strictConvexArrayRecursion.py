def findMinimum(arr, si, ei): 
    # Base Case: Only one element is present in arr[si..ei]*/ 
    if si == ei: 
        return arr[si] 
   
    # If there are two elements and first is lesser then 
    # the first element is minimum */ 
    if ei == si + 1 and arr[si] <= arr[ei]: 
        return arr[si]; 
   
    # If there are two elements and second is lesser then 
    # the second element is minimum */ 
    if ei == si + 1 and arr[si] > arr[ei]: 
        return arr[ei] 
   
    mid = (si + ei)//2   #si + (ei - si)/2;*/ 
   
    # If we reach a point where arr[mid] is greater than both of 
    # its adjacent elements arr[mid-1] and arr[mid+1], then arr[mid] 
    # is the maximum element*/ 
    if arr[mid] < arr[mid + 1] and arr[mid] < arr[mid - 1]: 
        return arr[mid] 
   
    # If arr[mid] is greater than the next element and smaller than the previous  
    # element then maximum lies on left side of mid */ 
    if arr[mid] < arr[mid + 1] and arr[mid] > arr[mid - 1]: 
        return findMinimum(arr, si, mid-1) 
    else: # when arr[mid] is greater than arr[mid-1] and smaller than arr[mid+1] 
        return findMinimum(arr, mid + 1, ei) 
   
# Driver program to check above functions */ 
# arr = [7, 5, 3, -1, -7, 5, 9, 100] #Solution is -7
# arr = [7, 5, 3, -1, -7] #Solution is -7
arr = [-7, 5, 9, 100] #Solution is -7
# arr = [5,-7] #Solution is -7
# arr = [-7,5] #Solution is -7
# arr = [-7] #Solution is -7
n = len(arr) 
print('List is: ',arr) 
print ("The minimum element is %d"% findMinimum(arr, 0, n-1))