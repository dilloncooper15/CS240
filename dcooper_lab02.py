# 1 - Chapter 3, exercises 6 and 7:


def grade_avg(grade1, grade2, grade3):
    """ (number, number, number) -> float

    Return the average of grade1, grade2, and grade 3, \
    where each grade rangesfrom 0 to 100, inclusive.

    >>> grade_avg(82, 19, 77)
    59.333333333333336
    >>> grade_avg(100, 90, 80)
    90.0
    >>> grade_avg(54, 67, 91)
    70.66666666666667
    """
    return (grade1 + grade2 + grade3) / 3


def top_three_avg(grade1, grade2, grade3, grade4):
    """ (number, number, number, number) -> float
    Return the best three grade's average from grade1, grade2, grade3,\
    and grade4.

    >>> top_three_avg(0, 70, 80, 90)
    80.0
    >>> top_three_avg(12, 24, 36, 48)
    36.0
    >>> top_three_avg(88, 46, 64, 73)
    75.0
    """
    sum_of_grades = grade1 + grade2 + grade3 + grade4
    top_three = sum_of_grades - min(grade1, grade2, grade3, grade4)
    return top_three / 3

# 2 - Chapter 5, exercise 8:


def convert_temperatures(t, source, target):
    """ (number, str, str) -> float
    Convert t from source units to target units and return the result.

    >>> convert_temperatures(100, 'Celsius', 'Fahrenheit')
    212.0
    >>> convert_temperatures(1, 'Reamur', 'Celsius')
    1.25
    >>> convert_temperatures(50, 'Celsius', 'Kelvin')
    323.15
    """
    if source == 'Kelvin':
        celsius = t - 273.15
    elif source == 'Celsius':
        celsius = t
    elif source == 'Fahrenheit':
        celsius = (t - 32) * 5 / 9
    elif source == 'Rankine':
        celsius = (t - 491.67) * 5 / 9
    elif source == 'Delisle':
        celsius = 100 - t * 2 / 3
    elif source == 'Newton':
        celsius = t * 100 / 33
    elif source == 'Reamur':
        celsius = t * 5 / 4
    elif source == 'Romer':
        celsius = (t - 7.5) * 40 / 21
    if target == 'Kelvin':
        return celsius + 273.15
    elif target == 'Celsius':
        return celsius
    elif target == 'Fahrenheit':
        return celsius * 9 / 5 + 32
    elif target == 'Rankine':
        return (celsius + 273.15) * 9 / 5
    elif target == 'Delisle':
        return (100 - celsius) * 3 / 2
    elif target == 'Newton':
        return celsius * 33 / 100
    elif target == 'Reamur':
        return celsius * 4 / 5
    elif target == 'Romer':
        return celsius * 21 / 40 + 7.5

# 3 - Chapter 6, exercise 3:


def average(num1, num2):
    """ (number, number) -> float

    Return the average of num1 and num 2.

    >>> average(10, 20)
    15.0
    >>> average(2.5, 3.0)
    2.75
    """

    return (num1 + num2) / 2

# 4 - Homework 02 Review:


def grades(days, student_id, homework_days):
    """ (int, str, int) -> list

    Given the number of days, studentid, and a list of homework days, \
    returns the nested list.

    >>> grades(25, 'jkruth', [1, 7, 14, 21])
    [25, ['jkruth', [1, 10, 10], [7, 10, 10], [14, 10, 10], [21, 10, 10]]]
    >>> grades(30, 'dcooper', [4, 8, 12, 16])
    [30, ['dcooper', [4, 10, 10], [8, 10, 10], [12, 10, 10], [16, 10, 10]]]
    """
    student = []
    a = []
    a.append(days)
    student.append(student_id)
    a.append(student)
    for day in homework_days:
        student.append([day, 10, 10])
    return a


# 5 - Chapter 9, Exercise 12:


def remove_neg(num_list):
    """ (list of number) -> NoneType

    Remove the negative numebrs from the list num_list.

    >>> num_list = [-5, 1, -3, 2]
    >>> num_list = [-2, 13, 55, 1]
    """
    index = 0
    while index < len(num_list):
        if num_list[index] < 0:
            del num_list[index]
        else:
            index += 1

if __name__ == '__main__':
    import doctest
    doctest.testmod()
