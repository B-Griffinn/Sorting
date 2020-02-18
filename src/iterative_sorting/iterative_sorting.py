# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    print(arr)
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i

        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index + 1, len(arr)):
            if arr[j] < arr[cur_index]:
                cur_index = j  


        # TO-DO: swap
        arr[i], arr[cur_index] = arr[cur_index], arr[i]
        

    return arr

my_arr = [2, 1, 3, 7, 9]
print(selection_sort(my_arr))


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr