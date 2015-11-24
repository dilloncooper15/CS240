class Score:
    """Creates the score class"""

    def __init__(self, points, initials):
        """(Score, int, str) -> Score

        Used for initializing Score objects. Takes the initials as a str and\
        the score as an int.
        """
        self.points = points
        self.initials = initials.upper()

    def __str__(self):
        """(Score) -> str

        Returns the string of the score and initials that are saved inside\
        the Score object.

        >>> str(Score(222, 'ABC'))
        '222 ABC'

        >>> str(Score(999, 'CBA'))
        '999 CBA'
        """
        return '{} {}'.format(self.points, self.initials)

    def __repr__(self):
        """(Score) -> str

        Returns the string of the input needed to generate the score object.

        >>> repr(Score(222, 'ABC'))
        "Score(222, 'ABC')"

        >>> repr(Score(999, 'CBA'))
        "Score(999, 'CBA')"
        """
        return "Score({}, '{}')".format(self.points, self.initials)

    def __lt__(self, obj):
        """(Score, Score) -> bool

        Deciphers if self is less than the Score obj. Returns True if and only\
        if self < obj and false for every other case. Compares numerical\
        values first, then compares initials.

        >>> Score(155, 'ABC') < Score(143, 'ABC')
        False
        >>> Score(625, 'ABC') < Score(701, 'ABC')
        True
        >>> Score(155, 'ABC') < Score(155, 'ABD')
        True
        >>> Score(155, 'XYZ') < Score(155, 'XYY')
        False
        >>> Score(155, 'XYZ') < Score(155, 'XYZ')
        False
        """
        return (self.points, self.initials) < (obj.points, obj.initials)

    def __gt__(self, obj):
        """(Score, Score) -> bool

        Deciphers if self is greater than the Score obj. Returns True if and\
        only if self > obj. Compares numerical values first, then compares\
        initials.

        >>> Score(155, 'ABC') > Score(143, 'ABC')
        True
        >>> Score(625, 'ABC') > Score(701, 'ABC')
        False
        >>> Score(155, 'ABC') > Score(155, 'ABD')
        False
        >>> Score(155, 'XYZ') > Score(155, 'XYY')
        True
        >>> Score(155, 'XYZ') > Score(155, 'XYZ')
        False
        """
        return (self.points, self.initials) > (obj.points, obj.initials)

    def __eq__(self, obj):
        """(Score, Score) -> bool

        Deciphers if self is equal to the Score obj. Compares numerical\
        values first then compares initials. If both are eqivalent, then\
        the statement will always return True. However, if they are not,\
        it will return False.

        >>> Score(155, 'ABC') == Score(143, 'ABC')
        False
        >>> Score(625, 'ABC') == Score(701, 'ABC')
        False
        >>> Score(155, 'ABC') == Score(155, 'ABD')
        False
        >>> Score(155, 'XYZ') == Score(155, 'XYY')
        False
        >>> Score(155, 'XYZ') == Score(155, 'XYZ')
        True
        """
        return (self.points, self.initials) == (obj.points, obj.initials)

    def __ne__(self, obj):
        """(Score, Score) -> bool

        Deciphers if self is not equal to the Score obj. Compares numerical\
        values first then compares initials. If both are not eqivalent, then\
        the statement will always return True. However, if they are not,\
        it will return False.

        >>> Score(155, 'ABC') != Score(143, 'ABC')
        True
        >>> Score(625, 'ABC') != Score(701, 'ABC')
        True
        >>> Score(155, 'ABC') != Score(155, 'ABD')
        True
        >>> Score(155, 'XYZ') != Score(155, 'XYY')
        True
        >>> Score(155, 'XYZ') != Score(155, 'XYZ')
        False
        """
        return not self == obj


class DetailedScore(Score):
    """initializes a score object via the Score class."""

    def __init__(self, points, initials, level):
        """(Score, int, str, int) -> None

        Initializes DetailedScore.
        """
        super().__init__(points, initials)
        self.level = level

    def __str__(self):
        """(DetailedScore) -> str

        Returns the string for the DetailedScore obj.

        >>> str(DetailedScore(155, 'ABC', 15))
        '155 ABC 2'
        """
        return '{} {} {}'.format(self.score, self.initials, self.level)

    def __repr__(self):
        """(DetailedScore) -> str

        Returns the str for DetailedScore.

        >>> repr(DetailedScore(155, 'ABC', 15))
        "DetailedScore(155, 'ABC', 15)"
        """
        return "DetailedScore({}, '{}', {})".format(self.score, self.initials,
                                                    self.level)


# def sort_scores(list1):
#     """(list of Scores) -> None

#     Utilizes sorts a list of scores.
#     """
#     sortval = list1[0]
#     sortind = 0
#     n = 0
#     while n < len(list1) - 1:
#         for index in range(n + 1, len(list1)):
#             if list1[n] > list1[index]:
#                 list1[n], list1[index] = list1[index], list1[n]
#         n += 1


def search_scores(list1, v):
    """(list of Scores, Score) -> index

    Uses binary search to analyze a list of scores and return the position of\
    the passed Score in the list. If the Score is not found, then it will\
    return the value -1.
    """

    start = 0
    end = len(list1) - 1
    while start < end:
        middle = end // 2
        if list1[middle] == v:
            return middle
        elif list1[middle] < v:
            start = middle + 1
        else:
            end = middle - 1
    return -1


if __name__ == '__main__':
    import doctest
    doctest.testmod()
