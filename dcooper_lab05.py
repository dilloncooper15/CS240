# Dillon J. Cooper
# CS 240 Lab 05

# Exercise 1: Implement a linear function using a loop called
# linear_loop_search.


def linear_loop_search(list_1, item_in_list):
    """ (list, int) -> int
    Returns the index of an item in the given list.

    >>> linear_loop_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 4)
    3
    >>> linear_loop_search([2, 4, 6, 8, 10, 12, 14, 16], 14)
    6
    >>> linear_loop_search([3, 9, 27, 81, 243, 729, 2187, 6561], 3)
    0
    """

    index = 0
    while index < len(list_1):
        if list_1[index] == item_in_list:
            return index
        else:
            index += 1
    return -1


# Exercise 2: Implement a linear search function using recursion called
# binary_recursive_search.


def linear_recursive_search(list_1, item_in_list):
    """ (list, int) -> int
    Returns the index of an item in the given sorted list.

    >>> linear_recursive_search([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 5)
    2
    >>> linear_recursive_search([11, 22, 33, 44, 55, 66, 77, 88, 99], 88)
    7
    >>> linear_recursive_search([2, 4, 8, 16, 32, 64, 128, 256, 512, 1024], 2)
    0
    """

    if len(list_1) < 1:
        return -1
    elif list_1[0] == item_in_list:
        return 0
    elif list_1[0] != item_in_list:
        a = linear_recursive_search(list_1[1:], item_in_list)
        if a == -1:
            return -1
        else:
            return a + 1


# Exercise 3: Implement a binary search function using a loop called
# binary_loop_search.


def binary_loop_search(list_1, item_in_list):
    """ (list, int) -> int
    Returns the index of an item in the given sorted list.

    >>> binary_loop_search([1, 6, 11, 16, 21, 26, 31, 36, 41, 46, 51], 26)
    5
    >>> binary_loop_search([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144], 2)
    3
    >>> binary_loop_search([2, 3, 5, 7, 11, 13, 17, 19, 23, 31, 37, 41], 37)
    10
    """

    first = 0
    last = len(list_1) - 1
    while first <= last:
        midpoint = (first + last) // 2
        if list_1[midpoint] == item_in_list:
            return midpoint
        elif list_1[midpoint] > item_in_list:
            last = midpoint - 1
        elif list_1[midpoint] < item_in_list:
            first = midpoint + 1
    return -1

# Exercise 4: Implement a (single) binary search function using recursion
# called binary_recursive_search.


def binary_recursive_search(list_1, item_in_list, first, last):
    """ (list, int, int, int) -> int
    Returns the index of an item, given a sorted list.

    >>> binary_recursive_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 0, 8)
    2
    >>> binary_recursive_search([1, 3, 5, 7, 9, 11, 13, 15], 9, 0, 7)
    4
    >>> binary_recursive_search([0, 1, 1, 2, 3, 5, 8, 13, 21, 34], 34, 0, 9)
    9
    >>> binary_recursive_search([0, 1, 1, 2, 3, 5, 8, 13, 21, 34], 21, 10, 9)
    -1
    """

    midpoint = (first + last) // 2
    if first > last:
        return -1
    elif list_1[midpoint] == item_in_list:
        return midpoint
    elif list_1[midpoint] > item_in_list:
        return binary_recursive_search(list_1, item_in_list, first,
                                       midpoint - 1)
    elif list_1[midpoint] < item_in_list:
        return binary_recursive_search(list_1, item_in_list, midpoint + 1,
                                       last)


# Exercise 5: Implement a driver function that uses your function from
# exercise 4 as a helper method. The driver function should use the same
# parameters (sometimes referred to as an interface) as exercises 1, 2 and 3.
# Name it binary_recursive_search_driver.


def binary_recursive_search_driver(list_1, item_in_list):
    """ (list, int) -> int
    Returns the index of an item, given a sorted list.

    >>> binary_recursive_search_driver([1, 2, 3, 4, 5, 6, 7, 8, 9], 5)
    4
    >>> binary_recursive_search_driver([1, 3, 5, 7, 9, 11, 13, 15], 13)
    6
    >>> binary_recursive_search_driver([3, 9, 27, 81, 243, 729, 2187], 729)
    5
    """

    return binary_recursive_search(list_1, item_in_list, 0, len(list_1) - 1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
