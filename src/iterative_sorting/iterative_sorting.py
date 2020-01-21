# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    for i in range(0, len(arr) - 1):
        # store current index on a var
        cur_index = i
        # track smallest index
        smallest_index = cur_index

        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for s in range(cur_index + 1, len(arr)):
            if arr[smallest_index] > arr[s]:
                smallest_index = s

        # TODO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    
    return arr





# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    x = True
    while x:
        x = False
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i + 1], arr[i] = arr[i], arr[i + 1]
                x = True

    return arr












# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr