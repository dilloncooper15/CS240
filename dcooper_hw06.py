def main():
    """
    Main logic of the program. Handles all input and output. Also builds the \
    shelves list.
    """
    shelf_range = ()
    shelves = []
    number_of_shelves = int(input('Number of shelves? '))
    print()
    for item in range(number_of_shelves):
        range_for_shelf = input('Range for shelf #{}: '.format(item + 1))
        range_for_shelf = range_for_shelf.split(', ')
        shelf_range = (range_for_shelf[0], range_for_shelf[1])
        shelves.append(shelf_range)
    print()
    author = input('Find author (enter nothing to quit): ')
    while author.strip() != '':
        response = search_shelves(author, shelves)
        print()
        print('Author: {}'.format(author))
        print('Shelf #: {}'.format(response[0] + 1))
        print('Shelves checked: {}'.format(response[1]))
        print()
        author = input('Find author (enter nothing to quit): ')
    print()


def check_shelf(author, shelf_range):
    """ (str, tuple) -> int
    Returns 0 if the author is on the shelf corresponding to the range. It \
    returns -1 if the author is on a shelf prior to the range, and 1 if the \
    author is on a shelf following the range.

    >>> check_shelf('Knuth, Donald', ('K', 'M'))
    0
    >>> check_shelf('Turning, Alan', ('Ba', 'Bn'))
    1
    >>> check_shelf('Engelbart, Douglas', ('Sab', 'Sim'))
    -1
    """
    author = author.upper()
    shelf_range_upper = (shelf_range[0].upper(), shelf_range[1].upper())
    if shelf_range_upper[0] <= author[0] <= shelf_range_upper[1]:
        return 0
    if shelf_range_upper[0] > author[0]:
        return -1
    if shelf_range_upper[1] < author[0]:
        return 1


def search_shelves(author, shelves):
    """ (str, list) -> list
    Returns a list index and the number of shelves checked.

    >>> shelves = [('A', 'D'), ('E', 'H'), ('I', 'L'), ('M', 'P'), ('Q', 'S'),\
                        ('T', 'V'), ('W', 'Z')]
    >>> search_shelves('Babbage, Charles', shelves)
    (0, 3)
    >>> search_shelves('Postel, Jon', shelves)
    (3, 1)
    """

    first = 0
    last = len(shelves) - 1
    count = 0
    while first <= last:
        count = count + 1
        midpoint = (first + last) // 2
        val = check_shelf(author, shelves[midpoint])
        if val == 0:
            return (midpoint, count)
        if val == 1:
            first = midpoint + 1
        if val == -1:
            last = midpoint - 1
    return -1, count

if __name__ == '__main__':
    main()
