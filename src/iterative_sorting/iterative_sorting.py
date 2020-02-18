# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    print(arr)
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i

        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)


        for j in range(cur_index + 1, len(arr)):
            # compare the index in our arr that is cur_index + 1 against the index in our array that is current index or the item to its left.
            if arr[j] < arr[cur_index]:

                # if the test above passes, update current index to equal the index `j` in our array
                cur_index = j

        # TO-DO: swap
        arr[i], arr[cur_index] = arr[cur_index], arr[i]
        

    return arr

my_arr = [2, 1, 3, 7, 9]
print(selection_sort(my_arr))


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    for i in range(len(arr) - 1, 0, -1):

        for j in range(i):

            if arr[j] > arr[j + 1]:

                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

    return arr

bub_arr = [2, 1, 3, 7, 9]
# arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# # arr2 = []
# # arr3 = [0, 1, 2, 3, 4, 5]
print(bubble_sort(bub_arr))


#############################
# ## INSERTION SORT

# my_list = [8, 2, 5, 4, 1, 3]


# def insertion_sort(arr):
#     # 1. seperate the first element from rest of the arr
#         # DONE IN STEP 2

#     # 2. for all other indicies, beginning with [1]:
#     for i in range(1, len(arr)):

#         # 2a. Copy the item at that index into a temp variable
#         temp = arr[i]
        
#         # 2b. Iterate to the left until you find the correct index in the "sorted" part of the array at which this element should be inserted
#         j = i
#         while j > 0 and temp < arr[j - 1]:
#             print(j)
            
#             ## shift items over to the right as you iterate
#             arr[j] = arr[j - 1]

#             # decrement j
#             j -= 1

#         # 2c. when the correct index is found, copy temp into this position
#         arr[j] = temp
    
#     return arr
# print(insertion_sort(my_list))