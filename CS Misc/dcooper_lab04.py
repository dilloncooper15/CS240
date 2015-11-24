# Dillon J. Cooper CS 240 Lab 03

# Exercise 1: Solve exercise 1 from Chapter 12. Post the answers to part a and\
# b in comments above your function.

# A) I would go through the the list and replace each character with it's\
# complement. That is, A replaced by T, T replaced by A, G replaced by C\
# and C replaced by G.
# B) No.
# C) (See function below)


def complement(sequence):
    """ str -> str

    Returns the complement of sequence.

    >>> complement('ATTGTTCAATT')
    'TAACAAGTTAA'
    >>> complement('AATTGCCGT')
    'TTAACGGCA'
    """

    complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    sequence_complement = ''

    for char in sequence:
        sequence_complement = sequence_complement + complement_dict[char]

    return sequence_complement


# Exercise 2: Solve exercise 3 from Chapter 12. Post the answer to part a in\
# comments above your function.

# A) index = 0
#    smallest = l[0]
#    for i in range(1, len(L)):
#       if L[i] < smallest:
#           index = i
#           smallest = L[i]

# B) (see function below)


def min_index(l):
    """ (list) -> tuple

    Return a tuple containing the minimum value in l its index.
    >>> min_index([15, 18, 14, 5, 13, 17, 44, 99, 2, 32])
    (2, 8)
    """

    index = 0
    smallest = l[0]

    for i in range(1, len(l)):
        if l[i] < smallest:
            index = i
            smallest = l[i]

    return (smallest, index)


# Exercise 3: A formula exists for calculating the amount of money in a\
# savings account that begins with an initial value (the initial principal, P)\
# and earns interest with an annual interest rate i, for n years: P(1+i)^n.\
# Write a recursive function called interest that calculates that same value,\
# and check your result against the formula.


def interest(p, i, n):
    """ float, float, float -> float
    Given the initial value 'p', annual interest rate 'i', for 'n' years,\
    return the amount of money in a savings account.

    >>> interest(100, .08, 5)
    633.5929036800001
    """

    if n == 0:
        return 0
    else:
        return p * (1 + i) ** n + interest(p, i, n - 1)


# Exercise 4: Here is a recursive definition to calculate a Fibonacci number n:

memory = {}


def fibonacci(n):
    """ int -> int
    Returns referenced, already calculated Fibonacci numbers.

    >>> fibonacci(5)
    8
    """

    if n == 0 or n == 1:
        return 1
    else:
        if n not in memory:
            memory[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return memory[n]

# Notice that each time a number is calculated, previous numbers are\
# recalculated. Modify your recursive function to remain previous, already\
# calculated Fibonacci numbers and reference them instead of recalculating\
# them. Hint: Use a global dictionary. (2 points)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
