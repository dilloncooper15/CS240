# Test II Study Guide


class A:
    __init__(self, ...)
    __str__(self)
    __repr__(self)
    __lt__(self, other)
    __gt__(self, other)
    __ne__(self, other)
    __eq__(self, other)


class B(A):
    __init__(self):
        super().__init__(self)


# Searching (Binary Search)
# Sorting (Selection Sort)
    # In the book, they sort numbers but for the test we\'re sorting a list of objects

# Additional Test help:

__gt__(self, other):
# Use if we are just comparing one attribute.
    return self.name > other.name
# Use if we are comparing more than one attribute (greater than OR equal to.)
    if self.name > other.name:
        return true
    elif self.name == other.name:
        if self.num > other.num:
            return true
        else:
            return false

__ne__(self, other):
    return self != other
# return self.name OR self.num OR etc. != other.name OR self.num OR etc.

__eq__(self, other):
    return self == other
# return self.name OR self.num OR etc. == other.name OR self.num OR etc.

__lt__:
        # if self.level < obj.level:
        #     return True
        # elif self.level == obj.level:
        #     if self.points < obj.points:
        #         return True
        #     elif self.points == obj.points:
        #         return self.initials < obj.initials


__gt__:
        # if self.level > obj.level:
        #     return True
        # elif self.level == obj.level:
        #     if self.points > obj.points:
        #         return True
        #     elif self.points == obj.points:
        #         return self.initials > obj.initials
