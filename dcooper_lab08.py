# Dillon J. Cooper
# CS 240 Lab 08

# Exercise 1: Write a class called Student that stores a student's last name
# (string), first name (string), ID (int). Make sure your class implements
# __init__, __str__, __repr__, __eq__, __ne__, __gt__, __ge__, __lt__, __le__.
# Comparison operators should base their comparison's first off the student's
# last name, first name, and with the student's ID. Equality functions can
# simply use the student's ID.


class Student:
    def __init__(self, last_name, first_name, stud_id):
        """(Student, str, str, int) -> NoneType

        Initalizes Student obj.
        """
        self.last_name = last_name
        self.first_name = first_name
        self.stud_id = stud_id

    def __str__(self):
        """(Student) -> str

        Returns a string of a student's last_name, first_name and stud_id.

        >>> str(Student('Smith', 'Josh', 98835))
        'Smith, Josh: 98835'
        >>> str(Student('Harrold', 'Vern', 11087))
        'Harrold, Vern: 11087'
        """
        return '{}, {}: {}'.format(
            self.last_name, self.first_name, self.stud_id)

    def __repr__(self):
        """(Student) -> str

        Returns a string of a student's last_name, first_name and stud_id.\
        This is need for the Student obj.

        >>> repr(Student('Smith', 'Josh', 98835))
        "Student('Smith', 'Josh', 98835)"
        >>> repr(Student('Harrold', 'Vern', 11087))
        "Student('Harrold', 'Vern', 11087)"
        """
        return "Student('{}', '{}', {})".format(
            self.last_name, self.first_name, self.stud_id)

    def __eq__(self, obj):
        """(Student, Student) -> bool

        Returns True if a student's ID matches a second student's ID. Returns\
        False, otherwise.

        >>> Student('Smith', 'Josh', 98835) == Student('Harold', 'Vern', 11087)
        False
        >>> Student('Adams', 'Cris', 19191) == Student('Adams', 'Cris', 19191)
        True
        >>> Student('Rock', 'Ty', 19192) == Student('Rock', 'Ty', 19193)
        False
        """
        return self.stud_id == obj.stud_id

    def __ne__(self, obj):
        """(Student, Student) -> bool

        Returns True if a student's ID does not match a second student's ID.\
        Returns False, otherwise.

        >>> Student('Smith', 'Josh', 98835) != Student('Harold', 'Vern', 11087)
        True
        >>> Student('Adams', 'Cris', 19191) != Student('Adams', 'Cris', 19191)
        False
        >>> Student('Rock', 'Ty', 19192) != Student('Rock', 'Ty', 19193)
        True
        """
        return self.stud_id != obj.stud_id
        # THIS ONE

    def __gt__(self, obj):
        """(Student, Student) -> bool

        Evaluates last_name first, first_name second and stud_id last. Returns\
        True if self.last_name > obj.last_name. If self.last_name ==\
        obj.last_name, then it will move on to compare first_name. That is, if\
        self.first_name > obj.first_name, then it will return True. If\
        self.first_name == obj.first_name, then it will return\
        self.stud_id > obj.stud_id.

        >>> Student('Smith', 'Josh', 98835) > Student('Harold', 'Vern', 11087)
        True
        >>> Student('Smith', 'Chris', 2222) > Student('Smith', 'Cris', 2222)
        False
        """
        if self.last_name > obj.last_name:
            return True
        elif self.last_name == obj.last_name:
            if self.first_name > obj.first_name:
                return True
            elif self.first_name == obj.first_name:
                if self.stud_id > obj.stud_id:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def __ge__(self, obj):
        """(Student, Student) -> bool

        Evaluates last_name first, first_name second and stud_id last. Returns\
        True if self >= obj and False, otherwise.

        >>> Student('Smith', 'Josh', 98835) >= Student('Smith', 'Vern', 11087)
        False
        >>> Student('Smith', 'Josh', 98835) >= Student('Rock', 'Vern', 11087)
        True
        >>> Student('Smith', 'Josh', 98835) >= Student('Smithy', 'Vern', 11087)
        False
        >>> Student('Smith', 'Josh', 98835) >= Student('Smith', 'Josh', 98835)
        True
        """
        if self == obj or self > obj:
            return True
        else:
            return False

    def __lt__(self, obj):
        """(Student, Student) -> bool

        Evaluates last_name first, first_name second and stud_id last. Returns\
        True if self.last_name < obj.last_name. If self.last_name ==\
        obj.last_name, then it will move on to compare first_name. That is, if\
        self.first_name < obj.first_name, then it will return True. If\
        self.first_name == obj.first_name, then it will return\
        self.stud_id < obj.stud_id.

        >>> Student('Smith', 'Josh', 98835) < Student('Harold', 'Vern', 11087)
        False
        """
        if self.last_name < obj.last_name:
            return True
        elif self.last_name == obj.last_name:
            if self.first_name < obj.first_name:
                return True
            elif self.first_name == obj.first_name:
                if self.stud_id < obj.stud_id:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def __le__(self, obj):
        """(Student, Student) -> bool

        Evaluates last_name first, first_name second and stud_id last. Returns\
        True if self <= obj and false, otherwise.

        >>> Student('Smith', 'Josh', 98835) <= Student('Smith', 'Vern', 11087)
        True
        >>> Student('Smith', 'Josh', 98835) <= Student('Rock', 'Vern', 11087)
        False
        >>> Student('Smith', 'Josh', 98835) <= Student('Smithy', 'Vern', 11087)
        True
        >>> Student('Smith', 'Josh', 98835) <= Student('Smith', 'Josh', 98835)
        True
        """
        if self == obj or self < obj:
            return True
        else:
            return False


# Exercise 2: Write a function called student_sort that uses merge sort to sort
# a list of Students.

def student_sort(students):
    """(list) -> list

    Utilizes merge sort to sort a list of students.
    """
    merge_sort = []
    for i in range(len(students)):
        merge_sort.append([students[i]])
    i = 0
    while i < len(merge_sort) - 1:
        students1 = merge_sort[i]
        students2 = merge_sort[i + 1]
        newl = merge(students1, students2)
        merge_sort.append(newl)
        i += 2
    if len(merge_sort) != 0:
        students[:] = merge_sort[-1][:]
    return students


def merge(l1, l2):
    """(list, list) -> list
    Sorts two lists and merges them into a single list.
    """
    roster = []
    i1 = 0
    i2 = 0
    while i1 < len(l1) and i2 < len(l2):
        if l1[i1] < l2[i2]:
            roster.append(l1[i1])
            i1 += 1
        else:
            roster.append(l2[i2])
            i2 += 1
    roster.extend(l1[i1:])
    roster.extend(l2[i2:])
    return roster


# Exercise 3: Write a function called student_search that uses a binary search
# to search your sorted listed of Students for a particular Student.

def student_search(students, v):
    """(list) -> index

    Utilizes a binary search to search the sorted list of Students for a\
    particular Student and returns the index of that Student.
    """
    initial = 0
    final = len(students) - 1
    while initial < final:
        mid = final // 2
        if students[mid] == v:
            return mid
        elif students[mid] < v:
            initial = mid + 1
        else:
            final = mid - 1
    return -1


# Exercise 4: Write a class called HonorStudent that inherits from student.
# HonorStudents have an addition attribute GPA (float). GPA does not influence
# the comparison and equality operators. Verify that your prior functions also
# work with a list of HonorStudents in your tests.

class HonorStudent(Student):
    """Creates an HonorStudent obj."""

    def __init__(self, last_name, first_name, stud_id, gpa):
        """(Student, str, str, int, float) -> NoneType

        Initalizes HonorStudent.
        """
        super().__init__(last_name, first_name, stud_id)
        self.gpa = gpa

if __name__ == '__main__':
    import doctest
    doctest.testmod()
