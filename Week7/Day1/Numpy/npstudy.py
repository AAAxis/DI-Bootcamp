import numpy as np

one_dim_array = np.arange(100)
def arr_stats(arr):
    min_val = np.min(arr)
    max_val = np.max(arr)
    std_val = np.std(arr)
    dot_val = np.dot(arr, arr)
    dot_itself_val = np.dot (arr, arr)
    substract_four = arr -4
    return F'''
    Min: {min_val}
    Max: {max_val}
    STD: {std_val}
    PROD: {dot_val}
    DOR_ITSELF: {dot_itself_val}
    SUBSTRACT_FOUR: {substract_four}
    '''
lst = [2,4,6]
arr = np.array(lst)
print(arr)


# * The minimum value in the array 
# * The standard deviation of the data 
# * The product of the elements in the array 
# * Dot product of the array to itself 
# * An array with 4 subtracted from every element in the input array
# one_dim_array

# two_dim_array = np.array ([[1,2,3,4]]), 