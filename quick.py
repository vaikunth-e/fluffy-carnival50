array = [8, 3, 5, 1, 6, 4, 9, 2, 7]
new_array = []
print(array)

# in place algoritm, recurvsive. arguments?
# some function to take an array fragment, do the sort, then hand back the fragment to the parent function

def quickSort(array):
    if len(array) <= 1: return array # end condition, if the array fragment is 1 or 0 elements, just pass it back
    pivot = array[len(array) - 1] # the pivot is the rightmost element in the array
    i = -1 # i starts as a pointer to before the first element
    j = 0 # j starts as a pointer to the first element

    # condition just ensures no out of bounds access (not needed? break statement in code handles loop exit case)
    while j < len(array):
        # checks if element j is less than or equal to pivot
        # if so, it moves i up 1, then swaps element i with element j
            # always happen. even when j is last element, this is executed before the loop breaks, which is why break cond isnt in loop conds
        # it performs a secondary check to see if j was pointing to the last element, if so, break cond met and breaks
        # i is currently pointing at the index where the pivot was sent to
        if array[j] <= pivot: 
            i += 1
            swap(i, j, array)
            if j == len(array) - 1: break
        j += 1
    print(array) # debug statement

    # we need to quick sort the left and right parts of the array, as defined by the pivots index (i).
    # we quickSort both parts indepedently. quickSort returns the concatenation of both sorted arrays
    # for the array[:i] quickSort will keep going deeper and deeper till only one element was passed to it, the pivot. at that point
    # the exit condition is met and the pivot gets returned to the left side, and the right side should also only have
    # been give one element so it too will return its element. since elements to the left of the pivot are always less than 
    # the pivot itself and elements to the right of it, given that there are two elements, if this was for the left original side
    # it will automatically be the two smallest elements which will have sort of bubbled to the side over multiple pivots
    return quickSort(array[:i]) + quickSort(array[i:])

def swap (i, j, array):
    temp = None
    temp = array[j]
    array[j] = array[i]
    array[i] = temp

print(quickSort(array))