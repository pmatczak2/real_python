student_grades = {
    "Jack": [85,95],
    "Jill": [80,95]
}

def get_grades_naice(name):
    if name in student_grades:
        return student_grades[name]
    return []

def get_grades_better(name):
    return student_grades.get(name,[])

def get_grades_wiht_assignment(name):
    if name not in student_grades:
        student_grades[name] = []
    return student_grades[name]

def set_grades_naive(name, score):
    if name in student_grades:
        grades = student_grades[name]
    else:
        student_grades[name] = []
        grades = student_grades[name]
    grades.append(score)-elfbm

def set_grade_better(name,score):
    grades = get_grades_wiht_assignment(name)
    grades.append(score)

set_grade_better("Jack", 100)
print(student_grades)