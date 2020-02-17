# TO-DO: Complete the selection_sort() function below 

def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        smallest_index = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)

        # create a var to hold right side of arr
            # then find the smallest element in that arr
        # right = arr[i + 1 : len(arr)]
        # loop through right and find smallest element
        for j in range(i + 1, len(arr)):
        # make comparison to current index
            if arr[j] < arr[smallest_index]:
                smallest_index = j
  
        # TO-DO: swap the curr index with the smallest element stored above
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i] 
    return arr

arr1 = [12, 1, 7]
print(selection_sort(arr1))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr