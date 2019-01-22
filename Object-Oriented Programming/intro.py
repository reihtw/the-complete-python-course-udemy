my_student = {
    'name': 'Rolf Smith',
    'grades': [70, 88, 90, 99]
}

def avarage_grade(student):
    return sum(student['grades']) / len(student['grades'])



class Student:
    def __init__(self, new_name, new_grades):
        self.name = new_name
        self.grades = new_grades
    
    def avarage(self):
        return sum(self.grades) / len(self.grades)

student_one = Student('Rolf Smith', [70, 88, 90, 99])

print(student_one.avarage())