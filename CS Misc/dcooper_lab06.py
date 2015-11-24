# Dillon J. Cooper
# CS 240 Lab 05

# Exercise 1: Complete exercise 5 from chapter 13. Include part a in the
# docstring of your function. Include part d as the doctests. Turn in only the
# documented function bubble_sort.


def bubble_sort(l):
    """(list) -> NoneType
    Compares every unsorted pair of elements in the list until every pair has\
    been compared:
        for every pair of elements that are unsorted:
            if the pair is not in the correct order:
                change to the correct order.

    >>> l = [1, 3, 5, 2, -2, 6]
    >>> print(bubble_sort(l))
    [-2, 1, 2, 3, 5, 6]
    >>> l = [10, 20, 30, 4, 8, 5, 56, 9]
    >>> print(bubble_sort(l))
    [4, 5, 8, 9, 10, 20, 30, 56]
    """

    last = len(l) - 1
    while last > 0:
        for i in range(0, last):
            if l[i] > l[i + 1]:
                p = l[i + 1]
                l[i + 1] = l[i]
                l[i] = p
        last = last - 1
    return l


# Exercise 2: Modify your function from the last exercise to sort a list of
# dictionaries. Each dictionary has the following keys: age, last_name,
# first_name. Sort in that same order. Name the function bubble_sort_dict.


def bubble_sort_dict(l):
    """(list of dicts) -> NoneType
    Sorts a list of dictionaries. Each dictionary has the following keys: age,\
    last_name, first_name, that are sorted in that order.

    >>> bubble_sort_dict([{'age': 20, 'last_name': 'Pi', 'first_name': 'JP'},
        {'age': 27, 'last_name': 'Lee', 'first_name': 'Chris'},
        {'age': 22, 'last_name': 'Lincoln', 'first_name': 'Abe'},
        {'age': 18, 'last_name': 'Brown', 'first_name': 'Travis'}])
    [{27, Lee, Chris}, {22, Lincoln, Abraham}, {20, Smith, Jeff},
    {18, Brown, Travis}]
    """

    last = len(l) - 1
    while last > 0:
        for i in range(0, last):
            if gt_lt(l[i], l[i + 1]):
                l[i], l[i + 1] = l[i + 1], l[i]
        last -= 1
    for dict in l:
        return 'age: {}, last_name: {}, first_name: {}'.format(
            dict['age'], dict['last_name'], dict['first_name'])


def gt_lt(dict1, dict2):
    """(dict, dict) -> Bool

    Compares the two dicts listed in the parameter, dict1 and dict2, by age\
    first, last_name, then first_name . If dict1 is larger, returns True.\
    If they are equal, then the next item will be compared. If dict1 is\
    smaller than dict2, returns false.

    >>> gt_lt({'age': 21, 'last_name': 'Norton', 'first_name': 'Josh'},
              {'age': 21, 'last_name': 'Smith', 'first_name': 'Josh'})
    False

    >>> gt_lt({'age': 21, 'last_name': 'Smith', 'first_name': 'Josh'},
                {'age': 12, 'last_name': 'Smith', 'first_name': 'Josh'})
    True

    >>> gt_lt({'age': 21, 'last_name': 'Smith', 'first_name': 'Jake'},
                {'age': 21, 'last_name': 'Smith', 'first_name': 'Josh'})
    False
    """

    if dict1['age'] > dict2['age']:
        return True
    elif dict1['age'] == dict2['age']:
        if dict1['last_name'] > dict2['last_name']:
            return True
        elif dict1['last_name'] == dict2['last_name']:
            if dict1['first_name'] > dict2['first_name']:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

# Exercise 3: Write an insertion sort algorithm to sort the same list of
# dictionaries referenced in the last exercise. Your sort function may share
# a comparison function with your bubble sort functions if you like. Name the
# function insertion_sort.


def insertion_sort(l):
    """(list of dicts) -> list of dicts

    Sorts a list utilizing insertion method. Check if item at index x is less\
    than the items before it and if it is less than the sorted portion of the\
    list. If this is the case, then x will be inserted into the correct\
    position.

    >>> insertion_sort([{'age': 35, 'last_name': 'Pi', 'first_name': 'Jim'},\
        {'age': 44, 'last_name': 'Owens', 'first_name': 'Tom'},\
        {'age': 55, 'last_name': 'Kringle', 'first_name': 'Chris'},\
        {'age': 21, 'last_name': 'Fox', 'first_name': 'Jason'},\
        {'age': 99, 'last_name': 'Mike', 'first_name': 'Mike'},\
        {'age': 44, 'last_name': 'Owens', 'first_name': 'Tim'},\
        {'age': 24, 'last_name': 'Adams', 'first_name': 'Ted'},\
        {'age': 26, 'last_name': 'Adams', 'first_name': 'Tom'}])
    [{'age': 21, 'last_name': 'Fox', 'first_name': 'Jason'},
    {'age': 24, 'last_name': 'Adams', 'first_name': 'Ted'},
    {'age': 26, 'last_name': 'Adams', 'first_name': 'Tom'},
    {'age': 35, 'last_name': 'Pi', 'first_name': 'Jim'},
    {'age': 44, 'last_name': 'Owens', 'first_name': 'Tim'},
    {'age': 44, 'last_name': 'Owens', 'first_name': 'Tom'},
    {'age': 55, 'last_name': 'Kringle', 'first_name': 'Chris'},
    {'age': 99, 'last_name': 'Mike', 'first_name': 'Mike'}]
    """

    i = 1
    while i != len(l):
        x = i
        while gt_lt(l[i - 1], l[x]) and i != 0:
            i -= 1
        value = l[x]
        del l[x]
        l.insert(i, value)
        i = x + 1
    for dict in l:
        return 'age: {}, last_name: {}, first_name: {}'.format(
            dict['age'], dict['last_name'], dict['first_name'])
    # return '{}, {}, {}'.format(l.key[0], l.key[1], l.key[2])
    # return '{}, {}, {}'.format(l[0], l[1], l[2])


if __name__ == '__main__':
    import doctest
    doctest.testmod()
