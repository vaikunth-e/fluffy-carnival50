array = [8, 3, 5, 1, 6, 4, 9, 2, 7]
new_array = []
print(array)

def mergeSort(array):
    if len(array) <= 1: return 
    k = len(array) // 2
    left = array[:k]
    right = array[k:]
    mergeSort(left)
    mergeSort(right)
    merge(left, right, array)

#slay

def merge(left, right, source):
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            source[k] = left[i]
            i += 1
            k += 1
        else:
            source[k] = right[j]
            j += 1
            k += 1
    
    while i < len(left):
        source[k] = left[i]
        i += 1
        k += 1
    
    while j < len(right):
        source[k] = right[j]
        j += 1
        k += 1

mergeSort(array)

print(array)