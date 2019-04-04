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
    # TODO: implement linear search recursively here
    pass
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


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





def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests
    if right == None:
        left = 0
        right = len(array) -1
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

    return binary_search_recursive(array, item, left, right)

my_array = [0,1,2,3,4,5,6,7,8,9]
print(binary_search_iterative(my_array, 8))