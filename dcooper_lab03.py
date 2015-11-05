# Dillon J. Cooper CS 240 Lab 03
# Exercise 1: Solve exercise 2 from Chapter 11.


def mating_pairs(males, females):
    """ (set, set) -> set of tuple

    Return a set of tuples containing one male from males and one female from\
    females.
    """

    pairs = set()
    num_gerbils = len(males)

    for i in range(num_gerbils):
        male = males.pop()
        female = females.pop()
        pairs.add((male, female),)
    return pairs


# Exercise 2: Solve exercise 5 from Chapter 11, but modify the function to\
# return the most likely, rather than the least likely.


def most_likely(probabilities):
    """ (dict of {str: float}) -> str

    Return the particle from probabilities with the highest probability.

    >>> most_likely({'neutron': 0.55, 'proton': 0.21, 'meson': 0.03,\
    'muron': 0.07, 'neutrino': 0.14})
    'neutron'
    """

    largest = 0
    name = ''

    for particle in probabilities:
        probability = probabilities[particle]
        if probability > largest:
            largest = probability
            name = particle
    return name


# Exercise 3: Solve exercise 8 from Chapter 11, but instead of dict_intersect,\
# write dict_sym_diff.


def dict_sym_diff(dict1, dict2):
    """ (dict, dict) -> dict

    Returns a dictionary that contains only the key/value pairs in one or\
    the other, but not both.
    """

    set_one = set(dict1.keys())
    set_two = set(dict2.keys())
    output = {}

    set_diff = set_one.symmetric_difference(set_two)
    for item in set_diff:
        if item in dict1.keys():
            output[item] = dict1[item]
        if item in dict2.keys():
            output[item] = dict2[item]
    return output


# Exercise 4: Solve exercise 9 from Chapter 11, but modify the db_headings\
# function to return keys that are common to all the inner dictionaries\
# (the intersection).


def db_headings(dict_of_dict):
    """ (dict of dict) -> set
    Return keys that are common to all of the inner dictionaries\
    (the intersection).

    >>> db_headings({'A': {1: 'a', 2: 'b'}, 'B': {2: 'c', 3: 'd'}})
    {2}
    """

    set_list = []
    for key in dict_of_dict.keys():
        set_list.append(set(dict_of_dict[key].keys()))
    for item in set_list[1:]:
        set_list[0] = set_list[0].intersection(item)
    return set_list[0]


# Exercise 5: Solve exercise 10 from Chapter 11, but instead of db_consistent,\
# write the function db_inconsistent.


def db_inconsistent(dict_of_dict):
    """ (dict of dict) -> set
    Takes a dictionary of dictionaries in dict_of_dict and returns True if\
    all the keys are not the same.

    >>> db_inconsistent({'A': {1: 'a', 2: 'b'}, 'B': {2: 'c', 3: 'd'}})
    True
    >>> db_inconsistent({'A': {1: 'a', 2: 'b'}, 'B': {2: 'c', 1: 'd'}})
    False
    """

    inner_keys_list = []
    for key in dict_of_dict:
        inner_keys = list(dict_of_dict[key].keys())
        inner_keys.sort()
        inner_keys_list.append(inner_keys)
    for i in range(1, len(inner_keys_list)):
        if len(inner_keys_list[0]) != len(inner_keys_list[i]):
            return True
        for j in range(len(inner_keys_list[0])):
            if inner_keys_list[0][j] != inner_keys_list[i][j]:
                return True
    return False


if __name__ == '__main__':
    import doctest
    doctest.testmod()
