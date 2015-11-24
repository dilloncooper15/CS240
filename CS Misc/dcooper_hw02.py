import math


def read_grades(grade_path):
    """(file open for reading) -> NoneType

    Returns a data structure containing the function's data.
    """

    grade_data = []
    student = []
    with open(grade_path, 'r') as gradebook:
        for line in gradebook:
            line = line.strip()
            line = line.split(' ')
            if line[0] == 'DAYS':
                grade_data.append(line[1])
            elif line[0] == 'STUDENT' and student == []:
                student.append(line[1])
            elif line[0] == 'STUDENT' and student != []:
                grade_data.append(student)
                student = []
                student.append(line[1])
            elif line[0] == 'GRADE':
                a, b, c, d, e = line
                c = int(c)
                d = int(d)
                e = int(e)
                student.append([c, d, e])
            else:
                continue
    grade_data.append(student)
    return grade_data


def summarize_grades(grades):
    """ (list) -> list

    Returns a list of student's grades starting with the student's id followed\
    by their midterm grade and final grade.

    >>> summarize_grades([90, ['jsmith', [10, 10, 8], [45, 100, 90],\
        [90, 200, 150]]])
    [['jsmith', 89.1, 80.0]]
    >>> summarize_grades([90, ['sjohnson', [10, 10, 9], [45, 100, 85],\
        [90, 200, 175]]])
    [['sjohnson', 85.5, 86.8]]
    >>> summarize_grades([90, ['dcooper', [10, 10, 9], [45, 100, 70],\
        [90, 200, 120]], ['jowens', [10, 10, 7], [45, 100, 88],\
        [90, 200, 100]]])
    [['dcooper', 71.8, 64.2], ['jowens', 86.4, 62.9]]
    """

    grade_data = []
    days = int(grades[0])
    student_grade = grades[1:]
    for student in student_grade:
        summaries = []
        summaries.append(student[0])
        midterm_date = math.ceil(days / 2)
        midterm_total = 0
        midterm_grade = 0
        final_total = 0
        final_grade = 0
        for work in student[1:]:
            if work[0] <= midterm_date:
                midterm_total = work[1] + midterm_total
                midterm_grade = work[2] + midterm_grade
            if work[0] <= days:
                final_total = work[1] + final_total
                final_grade = work[2] + final_grade
            else:
                continue
        calculated_midterm_grade = (midterm_grade / midterm_total)
        calculated_final_grade = (final_grade / final_total)
        summaries.append(round(calculated_midterm_grade * 100, 1))
        summaries.append(round(calculated_final_grade * 100, 1))
        grade_data.append(summaries)
    return grade_data


def write_summary(summary, summary_path):
    """(list) -> list

    Creates a new summary file that displays the student's id, midterm grade,\
    and final grade.
    """

    students = '{} {} {}\n'
    with open(summary_path, 'w') as outfile:
        for student in summary:
            student_list = students.format(student[0], student[1], student[2])
            outfile.write(student_list)

if __name__ == '__main__':
    grade_file = input('Enter a file path: ')
    grades = read_grades(grade_file)
    summary = summarize_grades(grades)
    summary_file = input('Enter an output file path: ')
    write_summary(summary, summary_file)
