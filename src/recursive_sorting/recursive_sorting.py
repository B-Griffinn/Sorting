# TO-DO: complete the helpe function below to merge 2 sorted arrays

### Step 1: split our lists into sublists until they are all length 1 or less
def merge_sort(arr):

    # Check if its length is 1 or less, if so return the list - bc sinlge item lists are sorted
    if len(arr) <= 1: # stopping recursion from infinite recursion - BASE CASE!!!
        return arr # if our arr length is <= 1 then it is already sorted and ready to use.

    # divide lists in half
    left = arr[ : len(arr) // 2] # slicing the arr into a left side
    right = arr[len(arr) // 2 : ] # slice the arr into a right side

    # Sort left side of list
    left = merge_sort(left) # use recursion to sort the left side of the arr
    
    # Sort the right side
    right = merge_sort(right) # use recursion to sort the left side of the arr

    # merge the two sorted sides together
    return merge(left, right) # our merge function in step two will accept the left arr and right arr appending them





########
### Step 2: Merge the two sorted sublists from above and return the sorted merge list
def merge(arr_a, arr_b):
    # hold total elemnts (length of both arrs) in a variable 
    total_elements = len(arr_a) + len(arr_b)
    merged_arr = [None] * total_elements

    # declare indicies for each sublist
    a = 0
    b = 0

    # loop through range of total_elements variable 
    for i in range(total_elements):

        # Check if either list is empty, if so append the other list
        if a >= len(arr_a): # if our indecies tracker is less than the length of our first given arr...
            merged_arr[i] = arr_b[b] # ...then update our merged_arr variable to = arr_a's index...
            b += 1 #... then increment b our other indecies tracker

        elif b >= len(arr_b):
            merged_arr[i] = arr_a[a]
            a += 1

        # otherwise, compare and append the smallest of the two lists
        elif arr_a[a] < arr_b[b]:
            merged_arr[i] = arr_a[a]
            a += 1

        else:
            merged_arr[i] = arr_b[b]
            b += 1

        # return our merged array
    return merged_arr


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
