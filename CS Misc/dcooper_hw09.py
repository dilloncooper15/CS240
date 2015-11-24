import io


class Gradebook:
    days = 0

    def __init__(self, file_name):
        self.file_name = file_name
        self.students = []
        with open(file_name, 'r') as data:
            for line in data:
                line = line.strip()
                line = line.split(' ')
                if line[0] == 'DAYS':
                    Gradebook.days = int(line[1])
                elif line[0] == 'STUDENT' and self.students == []:
                    s = Student(line[1], [])
                elif line[0] == 'STUDENT' and self.students != []:
                    self.students.append(s)
                    s = Student(line[1], [])
                elif line[0] == 'GRADE':
                    ger = Grade(line[1], line[2], line[3], line[4])
                    s.grades.append(ger)

    def write_summary(self, summary):
        with open(summary, 'w') as data:
            for student in self.students:
                data.write(str(student))


class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def midterm_grade(self):
        midterm_date = Gradebook.days // 2
        midterm_total = 0
        midterm_grade = 0
        for grade in self.grades:
            if grade.dueday <= midterm_date:
                midterm_total = grade.totalpoints + midterm_total
                midterm_grade = grade.earnedpoints + midterm_grade
        calculated_midterm_grade = (midterm_grade / midterm_total)
        return (round(calculated_midterm_grade * 100, 1))

    def final_grade(self):
        final_total = 0
        final_grade = 0
        for grade in self.grades:
            final_total = grade.totalpoints + final_total
            final_grade = grade.earnedpoints + final_grade
        calculated_final_grade = (final_grade / final_total)
        return (round(calculated_final_grade * 100, 1))

    def __str__(self):
        return '{} {} {}\n'.format(self.name, self.midterm_grade(),
                                   self.final_grade())


class Grade:
    """Creates an object for Grade."""
    def __init__(self, name, dueday, totalpoints, earnedpoints):
        """(Grade, str, int, int, int) -> None
        """
        self.name = name
        self.dueday = dueday
        self.totalpoints = totalpoints
        self.earnedpoints = earnedpoints


if __name__ == '__main__':
    main()
