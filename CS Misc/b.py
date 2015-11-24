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
