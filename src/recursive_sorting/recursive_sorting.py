# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    
    # create two indices to track for each arrays
        # initialize at 0
    index_a = 0 
    index_b = 0
    
    # the current index of the merged_arr (var) is the sum of the indices of arrA and arrB 
    ## starting at end of length of both arrs
    while (i := index_a + index_b) < elements: # elements == the length of both arrs sum 
    
        # test to see if we have reached the end of arrA
        try:
            # store current index of arrA on a var
            a = arrA[index_a]
        # if we have reached the end of arrA, fill with arrB
        except:
            merged_arr[i: ] = arrB[index_b: ]
            break 
            
        # test to see if we have reached the end of arrB
        try:
            # store current index of arrB on a var
            b = arrB[index_b]
        # if we reach the end of arrB, fill with arrA
        except:
            merged_arr[i: ] = arrA[index_a: ]
            break
        
        # if the values of a and b are == add them both to the merged_arr var
        # then skip the next index; otherwise add the lesser values
        if a <= b:
            merged_arr[i] = a
            index_a += 1
            i += 1
        if b <= a:
            merged_arr[i] = b
            index_b += 1
            i += 1
    return merged_arr
        
        
    
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):

    # BASE CASE
    if len(arr) <= 1:
        return arr

    #SPLIT left side of arr
    left = arr[ : len(arr) // 2 ]

    #SPLIT right side of arr
    right = arr[len(arr) // 2 : ]
    
    # Create a recursive case in order to update left and right
    left = merge_sort(left)
    right = merge_sort(right)
    
    # return our merge function in order to sort the two arrs together
    return merge(left, right)

arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
merge_sort(arr1), [0,1,2,3,4,5,6,7,8,9]