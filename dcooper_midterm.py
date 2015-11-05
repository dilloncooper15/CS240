# Dillon J. Cooper
# CS 240 Midterm

# Exercise 1:


def upper_file(y, z):
    """ str, str -> Nonetype

    Given a string containing a source filename and a string containing a\
    destination filename, opens the source file, reads and converts all the\
    text to uppercase, and saves it to the destination file. Returns nothing.
    """
    var = []
    with open(y, 'r') as inputfile:
        var = inputfile.read().upper()
        with open(z, 'w') as outputfile:
            for item in var:
                outputfile.write(item)


# Exercise 2:

def csv_parse(d):
    """ str -> tuple
    Given a string containing a source filename, parses a CSV file, returning\
    a tuple containing two lists.
    """

    second_list = []
    tuple_1 = ()

    with open(d, 'r') as inputfile:
        var = inputfile.readline().strip().split(',')
        second_line = inputfile.readlines()
        for item in second_line:
            item = item.strip()
            item = item.split(',')
            second_list.append(item)
        tuple_1 = (var, second_list)
        return tuple_1


# Exercise 3:

def common_birds():
    """ (list), (list) -> set()
    Given two lists of string containing bird names, returns a set of unique\
    bird names (no duplicates) common to both bird watcher's lists.
    """

    list_1 = []
    list_2 = []
    w = set()

    for item in list_1:
        if item in list_2:
            w.add(item)
    return w


# Exercise 4:

def csv_parse_dict(d):
    """ str -> (list of dicts)
    Given a string containing a source filename, parses a CSV file, returning\
    a list of dictionaries.
    """

    a = []

    with open(d, 'r') as inputfile:
        var = inputfile.readline().strip().split(',')
        second_line = inputfile.readlines()
        for item in second_line:
            item = item.strip()
            item = item.split(',')
            b = dict()
            for thing in item:
                key = var[item.index(thing)]
                b[key] = thing
            a.append(b)
        return a


# Exercise 5:

def rot13(char):
    char = char.upper()
    if char.isalpha():
        return chr((((ord(char) - ord('A') + 13) % 26) + ord('A')))
    else:
        return char


def rot13str(l):
    """ str -> str
    Accepts a string as a parameter and returns an encrypted string.
    """

    if len(l) == 1:
        return rot13(l)
    else:
        return rot13(l[0]) + rot13str(l[1:])
