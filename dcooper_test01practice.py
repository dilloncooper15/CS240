# Chapter 11, Exercise 1


def find_dups(l):
    """ (list) -> set

    Returns a set of integers that occur two or more times in l.

    >>> find_dups([1, 2, 3, 4, 1, 2, 8])
    {1, 2}
    """
    elem_set = set()
    dups_set = set()

    for entry in l:
        len_initial = len(elem_set)
        elem_set.add(entry)
        len_after = len(elem_set)
        if len_initial == len_after:
            dups_set.add(entry)
    return(dups_set)


# Chapter 11, Exercise 4


def count_values(dictionary):
    """ (dict) -> int

    Return the number of distinct values in dictionary.

    >>> count_values({'red': 1, 'green': 1, 'blue': 2})
    2
    """

    return len(set(dictionary.values()))


def count_duplicates(dictionary):
    """ (dic) -> int

    Return the number of duplicate values in dictionary.

    >>> count_duplicates({'a': 1, 'b': 2, 'c': 3, 'd': 1, 'e': 3})
    2
    """

    duplicates = 0
    values = list(dictionary.values())

    for item in values:
        if values.count(item) >= 2:
            duplicates = duplicates + 1
            num_occurrences = values.count(item)
            for i in range(num_occurrences):
                values.remove(item)
    return duplicates


if __name__ == '__main__':
    import doctest
    doctest.testmod()
