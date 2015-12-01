# Dillon J. Cooper
# Computer Science II, Test II


class Score:
    """ Creates the score class. """

    def __init__(self, points, initials):
        """(Score, int, str) -> Score

        Used to initialize Score objects. Also takes the initials as a str and\
        score as an int.
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
        return (self.points, self.initials) != (obj.points, obj.initials)


def find_min(scorelist, p):
    """ (list, int) -> int

    Returns the index of the smallest value that's in scorelist[p:]

    >>> find_min([9, 7, 3, 5, 11, 4], 0)
    2
    >>> find_min([12, 22, 1, 2, 3, 5], 0)
    2
    >>> find_min([99, 1, -2, 22, 68, -99], 0)
    5
    """
    smallest = p
    i = p + 1
    while i != len(scorelist):
        if scorelist[i] < scorelist[smallest]:
            smallest = i
        i += 1
    return smallest


def sort_scores(scorelist):
    """(list) -> list
    Given a list of Scores, sort_scores sorts the list according to points\
    first and then initials. This function mutates the list rather than\
    returning a new list. Groups by level first, followed by points and\
    then initials.

    >>> a = Score(100, 'DEL')
    >>> b = Score(90, 'JDK')
    >>> c = Score(80, 'ZGK')
    >>> d = Score(70, 'ABC')
    >>> scorelist = [a, b, c, d]
    >>> sort_scores(scorelist)
    >>> print(scorelist)
    [Score(70, 'ABC'), Score(80, 'ZGK'), Score(90, 'JDK'), Score(100, 'DEL')]
    """
    i = 0
    while i != len(scorelist):
        smallest = find_min(scorelist, i)
        scorelist[i], scorelist[smallest] = scorelist[smallest], scorelist[i]
        i += 1


def search_scores(scorelist, v):
    """(list, int) -> index

    Uses binary search to analyze a list of scores and return the position of\
    the passed Score in the list. If the score is not found, then it will\
    return the value -1.

    >>> a = DetailedScore(100, 'DEL', 2)
    >>> b = DetailedScore(90, 'JDK', 3)
    >>> c = DetailedScore(80, 'ZGK', 1)
    >>> d = DetailedScore(70, 'ACB', 2)
    >>> e = DetailedScore(100, 'NAM', 3)
    >>> scorelist = [a, b, c, d, e]
    >>> sort_scores(scorelist)
    >>> print(search_scores(scorelist, a))
    2
    """
    start = 0
    end = len(scorelist) - 1
    while start != end + 1:
        middle = (start + end) // 2
        if scorelist[middle] < v:
            start = middle + 1
        else:
            end = middle - 1
    if 0 <= start < len(scorelist) and scorelist[start] == v:
        return start
    else:
        return -1


class DetailedScore(Score):
    """ Initializes a score object via the Score class. """

    def __init__(self, points, initials, level):
        """(Score, int, str, int) -> NoneType

        Initializes DetailedScore.
        """
        super().__init__(points, initials)
        self.level = level

    def __str__(self):
        """(self) -> str

        Returns a string for the DetailedScore.

        >>> str(DetailedScore(100, 'DEL', 2))
        '100 DEL 2'
        >>> str(DetailedScore(90, 'JDK', 3))
        '90 JDK 3'
        >>> str(DetailedScore(80, 'ZGK', 1))
        '80 ZGK 1'
        """
        return super().__str__() + ' {}'.format(self.level)

    def __repr__(self):
        """(self) -> str

        Returns a str for DetailedScore.

        >>> repr(DetailedScore(100, 'DEL', 2))
        'DetailedScore(100, DEL, 2)'
        >>> repr(DetailedScore(90, 'JDK', 3))
        'DetailedScore(90, JDK, 3)'
        >>> repr(DetailedScore(80, 'ZGK', 1))
        'DetailedScore(80, ZGK, 1)'
        """
        return 'DetailedScore({}, {}, {})'.format(self.points, self.initials,
                                                  self.level)

    def __lt__(self, obj):
        """(DetailedScore, DetailedScore, DetailedScore) -> bool

        Evaluates level first, points second and initials last. Returns True\
        if self.level < obj.level. If self.level == obj.level, then it will\
        move on to compare points. That is, if self.points < obj.points, then\
        it will return True. If self.points == obj.points, then it will return\
        self.initials < obj.initials.

        >>> a = DetailedScore(100, 'DEL', 2)
        >>> b = DetailedScore(90, 'JDK', 3)
        >>> c = DetailedScore(80, 'ZGK', 1)
        >>> d = DetailedScore(70, 'ACB', 2)
        >>> e = DetailedScore(100, 'NAM', 3)
        >>> a < b
        True
        >>> c < d
        True
        >>> e < a
        False
        """
        if self.level < obj.level:
            return True
        elif self.level == obj.level:
            if self.points < obj.points:
                return True
            elif self.points == obj.points:
                if self.initials < obj.initials:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def __gt__(self, obj):
        """(DetailedScore, DetailedScore, DetailedScore) -> bool

        Evaluates level first, points second and initials last. Returns True\
        if self.level > obj.level. If self.level == obj.level, then it will\
        move on to compare points. That is, if self.points > obj.points, then\
        it will return True. If self.points == obj.points, then it will return\
        self.initials > obj.initials.

        >>> a = DetailedScore(100, 'DEL', 2)
        >>> b = DetailedScore(90, 'JDK', 3)
        >>> c = DetailedScore(80, 'ZGK', 1)
        >>> d = DetailedScore(70, 'ACB', 2)
        >>> e = DetailedScore(100, 'NAM', 3)
        >>> f = DetailedScore(90, 'BAC', 3)
        >>> b > c
        True
        >>> e > a
        True
        >>> a > d
        True
        >>> f > b
        False
        """
        if self.level > obj.level:
            return True
        elif self.level == obj.level:
            if self.points > obj.points:
                return True
            elif self.points == obj.points:
                if self.initials > obj.initials:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def __ne__(self, obj):
        """(DetailedScore, DetailedScore, DetailedScore) -> bool

        Evaluates level first, points second and initials last. Returns True\
        if self != obj. Returns False otherwise.

        >>> a = DetailedScore(100, 'DEL', 2)
        >>> b = DetailedScore(90, 'JDK', 3)
        >>> c = DetailedScore(80, 'ZGK', 1)
        >>> d = DetailedScore(70, 'ACB', 2)
        >>> e = DetailedScore(100, 'NAM', 3)
        >>> f = DetailedScore(90, 'JDK', 3)
        >>> b != c
        True
        >>> a != e
        True
        >>> a != c
        True
        >>> f != b
        False
        """
        if self.level != obj.level:
            return True
        elif self.level == obj.level:
            if self.points != obj.points:
                return True
            elif self.points == obj.points:
                if self.initials != obj.initials:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def __eq__(self, obj):
        """(DetailedScore, DetailedScore, DetailedScore) -> bool

        Evaluates level first, points second and initials last. Returns True\
        if self == obj. Returns False otherwise.

        >>> a = DetailedScore(100, 'DEL', 2)
        >>> b = DetailedScore(90, 'JDK', 3)
        >>> c = DetailedScore(80, 'ZGK', 1)
        >>> d = DetailedScore(70, 'ACB', 2)
        >>> e = DetailedScore(100, 'NAM', 3)
        >>> f = DetailedScore(90, 'JDK', 3)
        >>> b == f
        True
        >>> a == a
        True
        >>> d == c
        False
        >>> a == e
        True
        """
        if self.level == obj.level:
            return True
        elif self.level != obj.level:
            if self.points == obj.points:
                return True
            elif self.points != obj.points:
                if self.initials == obj.initials:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False


if __name__ == '__main__':
    import doctest
    doctest.testmod()
