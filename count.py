array = [8, 3, 5, 1, 6, 4, 9, 2, 7]
range = 9
print(array)

# requires knowing range of data?
# in lang w/o dynamically allocated arrays?
def countSort(array, range):
    count_array = [0] * (range + 1)
    for element in array: count_array[element] += 1
    