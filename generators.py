# Generators are a useful way to iterate through a sequence using constant memory.
# Here’s an example:
student_grades = {
    "pete": [80, 56],
    "cat": [55, 3]
}


def get_grades_naive(name):
    if name in student_grades:
        return student_grades[name]
    return []


def get_grades_bette(nema):
    return student_grades.get(nema, [])


def set_grade_naive(name, score):
    if name in student_grades:
        grade = student_grades[name]
    else:
        student_grades[name] = []
        grade = student_grades[name]
    grade.append(score)


set_grade_naive("pete", 100)

print(student_grades)
