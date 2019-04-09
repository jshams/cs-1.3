#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_iterative(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    return None if index == len(array) else index if array[index] == item else linear_search_recursive(array, item, index + 1)
    
    '''this (above) is that (below)'''
    # if array[index] == item:
    #     return index
    # if index == len(array) - 1:
    #     return None
    # return linear_search_recursive(array, item, index + 1)

def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests
    left = 0
    right = len(array) - 1

    while True:
        median = (right + left) // 2
        median_value = array[median]
        if median_value == item:
            return median
        if item > median_value:
            left = median + 1
        elif item < median_value:
            right = median - 1
        if right == left:
            if array[left] == item:
                return right
            return None

def binary_search_recursive(array, item, left=0, right=None):

    if right == None: # checks if were beggining sets the values of left and right
        # left = 0
        right = len(array) -1
    elif left > right: # will end the program if left is greater than right (intsersecting)
        return None
    median = (right + left) // 2 # finds the median (floored average of right and left)
    median_value = array[median] # this is the value of the item were indexing 
    if median_value == item: # checks if the median is the item we're looking for
        return median
    elif item > median_value: # if the item is greater than the median our left = median + 1
        left = median + 1
    elif item < median_value: # if the item is less than the median our right = median - 1
        right = median - 1
    # if right == left:
    #     if array[left] == item:
    #         return left
    #     return None
    return binary_search_recursive(array, item, left, right)


def ratio_search_recursive(array, item, left=None, right=None):
    ''' This method is similar to the binary search method, 
    but instead of splitting the array by the center we use ratios instead
    the fastest this will run is O(1) and the slowest is O(n)
    This function works best when the median is closer to the mean 
    Will work even better when the median close to half of the largest value
    '''
    # print("Yup")
    if right == None: # checks if we're beggining
        left = 0
        right = len(array) -1
    median = (right - left) * (item // array[right] - array[left]) + left
    median_value = array[median]
    if median_value == item:
        return median
    if item > median_value:
        left = median + 1
    elif item < median_value:
        right = median - 1
    if right == left:
        if array[left] == item:
            return right
        return None
    return ratio_search_recursive(array, item, left, right)


my_array = [0, 1, 5, 10, 22, 25, 29, 37, 38, 39,40,41 ,42, 43, 44, 45, 46, 69, 72, 86, 96, 100,101,102,103,104,105,106,107,108,110,111,112,113,114,115,116,121,122,123,132,133,134,135,154]
print(binary_search_recursive(my_array, 44))