
def read_grades(grade_path):
    """(file open for reading) -> NoneType

    Returns a data structure containing the function's data.
    """

    with open(grade_path, 'r') as gradebook:
        grade_data = {}
        for line in gradebook:
            line = line.strip()
            line = line.split(' ')
            if line[0] == 'DAYS':
                grade_data['DAYS'] == line[1]
            elif line[0] == 'STUDENT':
                name = line[1]
                grade_data[name] == {}
            elif line[0] == 'GRADE':
                student_grade = len(grade_data[name])
                grade_data[name][student_grade] = {'due_date': line[2],
                                                   'points_possible': line[3],
                                                   'points_earned': line[4]}
    return(grade_data)


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

    days = int(grades[0])
    student_grade = grades[1]
    summaries = {}
    for student in student_grade:
        midterm_grade = [0, 0]
        final_grade = [0, 0]
        for work in student_grade[student]:
            if work[0] <= (days / 2):
                midterm_grade[0] = midterm_grade[0] + work[-1]
                midterm_grade[1] = midterm_grade[1] + work[-2]
                final_grade[0] = final_grade[0] + work[-1]
                final_grade[1] = final_grade[1] + work[-2]
            elif work[0] <= days:
                final_grade[0] = final_grade[0] + work[-1]
                final_grade[1] = final_grade[1] + work[-2]
            else:
                continue
        calculated_midterm_grade = (midterm_grade[0] / midterm_grade[1]) * 100
        calculated_final_grade = (final_grade[0] / final_grade[1]) * 100
        summaries[student] = (round(calculated_midterm_grade, 1),
                              round(calculated_final_grade, 1))
    return summaries


def write_summary(summary, summary_path):
    """(list) -> list

    Creates a new summary file that displays the student's id, midterm grade,\
    and final grade.
    """

    students = '{} {} {}\n'
    with open(summary_path, 'w') as outfile:
        for item in summary.keys():
            outfile.write(students.format(item, summary[item][0],
                                          summary[item][1]))

if __name__ == '__main__':
    grade_file = input('Enter a file path: ')
    grades = read_grades(grade_file)
    summary = summarize_grades(grades)
    summary_file = input('Enter an output file path: ')
    write_summary(summary, summary_file)
