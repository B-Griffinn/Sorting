# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    
    # create new array size of the lengths of doth data sets
    elements = len( arrA ) + len( arrB )
    merged_arr = [None] * elements

    a = 0
    b = 0

    # TO-DO
    for i in range(elements):

        # if all el in arrA have been merged, put next el in arrB into merged_arr
        if a >= len(arrA):
            merged_arr[i] = arrB[b]
            b += 1
        
        elif b >= len(arrB):
            merged_arr[i] = arrA[a]
            a += 1
        # if nex element is arrA is smaller add to merged arr
        elif arrA[a] < arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1

        else:
            merged_arr[i] = arrB[b]
            b += 1

        # if nex element is arrB is smaller add to merged arr

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    # base case if len of arr is 0 or 1
    if len(arr) <= 1:
        return arr

    left = merge_sort(arr[ : len(arr) // 2]) # slice arr to make left hand side
    right = merge_sort(arr[len(arr) // 2 : ]) # slice arr to make right hand side

    print("Left: " , left)
    print("Right: " , right)

    return merge(left, right)


print(merge_sort([2, 1, 5, 4, 3]))






# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr