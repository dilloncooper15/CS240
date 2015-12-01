# Dillon J. Cooper
# CS 240 Homework 7


def main():
    """(NoneType) -> NoneType
    The main logic of the program. Prompts the user to input students \
    information in the following format: \
    house, year, last name, first name. \
    Main() handles all the input and output.
    """

    roster = []
    student = input('Enter a student record (blank to end): ')
    while student.strip() != '':
        roster.append(tuple(student.split(', ')))
        student = input('Enter a student record (blank to end): ')
    new_list = sort_students(roster)
    print()
    for student in new_list:
        print('{}, {}, {}, {}'.format(student[0], student[1], student[2],
                                      student[3]))


def sort_students(roster):
    """ (list of tuples) -> list of tuples

    Given a roster which is a list of tuples, returns a new list, sorted by\
    house, year, last name, and first name.

    >>> sort_students([('Hufflin', '2', 'Measely', 'Don'), \
('Gryffinpuff', '2', 'Cotter', 'Terry'), \
('Hufflin', '2', 'Measely', 'Winny'), \
('Slytherclaw', '1', 'Hickory', 'Frederick'), \
('Ravendor', '3', 'Danger', 'Harmony'), \
('Gryffinpuff', '1', 'Dovewood', 'Juna'), \
('Ravendor', '7', 'Cotter', 'Tilly'), \
('Slytherclaw', '6', 'Alloy', 'Franco')])
    [('Gryffinpuff', '1', 'Dovewood', 'Juna'), \
('Gryffinpuff', '2', 'Cotter', 'Terry'), \
('Hufflin', '2', 'Measely', 'Don'), \
('Hufflin', '2', 'Measely', 'Winny'), \
('Ravendor', '3', 'Danger', 'Harmony'), \
('Ravendor', '7', 'Cotter', 'Tilly'), \
('Slytherclaw', '1', 'Hickory', 'Frederick'), \
('Slytherclaw', '6', 'Alloy', 'Franco')]
    """

    merge_sort = []
    for i in range(len(roster)):
        merge_sort.append([roster[i]])
    i = 0
    while i < len(merge_sort) - 1:
        a1 = merge_sort[i]
        a2 = merge_sort[i + 1]
        newl = merge(a1, a2)
        merge_sort.append(newl)
        i += 2
    if len(merge_sort) != 0:
        roster[:] = merge_sort[-1][:]
    return roster


# merging lists
def merge(l1, l2):
    """ (list, list) -> list

    Merges two lists into a new list. Returns the new list.

    >>> merge([('Gryffinpuff', '1', 'Dovewood', 'Juna')], \
        [('Slytherclaw', '1', 'Hickory', 'Frederick')])
    [('Gryffinpuff', '1', 'Dovewood', 'Juna'), \
('Slytherclaw', '1', 'Hickory', 'Frederick')]
    """

    roster = []
    i1 = 0
    i2 = 0
    while i1 != len(l1) and i2 != len(l2):
        if rank(l1[i1], l2[i2]):
            roster.append(l1[i1])
            i1 += 1
        else:
            roster.append(l2[i2])
            i2 += 1
    roster.extend(l1[i1:])
    roster.extend(l2[i2:])
    return roster


def rank(item1, item2):
    """(tuple, tuple) -> bool or str

    Returns True if item1 is less than item2 and returns False if item1 is\
    greater than item2.

    >>> rank(('Hufflin', '2', 'Measely', 'Don'), \
        ('Slytherclaw', '1', 'Hickory', 'Frederick'))
    True
    >>> rank(('Ravendor', '7', 'Cotter', 'Tilly'), \
        ('Hufflin', '2', 'Measely', 'Winny'))
    False
    """
    if item1[0] < item2[0]:
        return True
    if item1[0] > item2[0]:
        return False
    else:
        if item1[1] < item2[1]:
            return True
        if item1[1] > item2[1]:
            return False
        else:
            if item1[2] < item2[2]:
                return True
            if item1[2] > item2[2]:
                return False
            else:
                if item1[3] < item2[3]:
                    return True
                if item1[3] > item2[3]:
                    return False
                else:
                    if item1[4] < item2[4]:
                        return True
                    if item1[4] > item2[4]:
                        return False


if __name__ == '__main__':
    main()
