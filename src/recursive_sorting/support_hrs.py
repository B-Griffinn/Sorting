# TO-DO: complete the helpe function below to merge 2 sorted arrays
arr1 = [1, 2]
arr2 = [3, 4]

def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO

    # create pointer variables for each arr to store beginning index/cur index
    pointer_1 = 0
    pointer_2 = 0

    # loop through both arrs using pointers to find smallest element
    # look at first element in each arr and set smallest to the left of arr1

    for i in range(elements):
        # if out of range handle pointers
        if len(arrA) >= pointer_1:
            merged_arr[i] = arrB[pointer_2]
            pointer_2 += 1

        # if out of range handle pointers 
        if len(arrB) >= pointer_2:
            merged_arr[i] = arrA[pointer_1]
            pointer_1 += 1

        # if index[0] of arrA < index of arrB[0]
            # then place arrA index[0] at beginning of merged arr
            # merge the smaller elements into a new list
        if arrA[pointer_1] < arrB[pointer_2]:
            merged_arr[i] = arrA[pointer_1]
            pointer_1 += 1

        elif arrB[pointer_2] < arrA[pointer_1]:
            merged_arr[i] = arrB[pointer_2]
            pointer_2 += 1

    return merged_arr

















# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
     
    # 1 Create a base case
    if len(arr) <= 1:
        return arr 

    #SPLIT arr in two halfs
    mid = len(arr) // 2
    left = merge_sort(arr[ : mid])
    right = merge_sort(arr[mid : ])

    # left = arr[ : len(arr) // 2]
    # right = arr[len(arr) // 2 : ]
  
    return merge(left, right)