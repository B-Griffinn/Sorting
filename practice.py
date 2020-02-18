arr = [5, 3, 8, 6, 7, 2]

def selection_sort(nums):

    for i in range(5):

        # var to hold min position
        min_pos = i         # starts at 0
        
        for j in range(i, 6):

            # find min value
            if nums[j] < nums[min_pos]:
                # new position!!
                min_pos = j
        
        # SWAPpin only once!
        temp = nums[i]
        nums[i] = nums[min_pos]
        nums[min_pos] = temp

        print(nums)

    return arr

print(selection_sort(arr))