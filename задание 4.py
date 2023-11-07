
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_avg_grade(self):
        return sum(self.grades) / len(self.grades)


class Lecturer:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_avg_grade(self):
        return sum(self.grades) / len(self.grades)


class Course:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.lecturers = []

    def add_student(self, student):
        self.students.append(student)

    def add_lecturer(self, lecturer):
        self.lecturers.append(lecturer)


def calculate_avg_homework_grade(students, course_name):
    grades = []
    for student in students:
        grades.extend(student.grades)
    return sum(grades) / len(grades)


def calculate_avg_lecture_grade(lecturers, course_name):
    grades = []
    for lecturer in lecturers:
        grades.extend(lecturer.grades)
    return sum(grades) / len(grades)


# Создание экземпляров классов
student1 = Student("Иванов")
student2 = Student("Петров")
lecturer1 = Lecturer("Сидоров")
lecturer2 = Lecturer("Васильев")
course1 = Course("Python")
course2 = Course("Data Science")

# Присоединение студентов и лекторов к курсам
course1.add_student(student1)
course1.add_student(student2)
course2.add_student(student1)
course2.add_student(student2)
course1.add_lecturer(lecturer1)
course2.add_lecturer(lecturer1)
course1.add_lecturer(lecturer2)
course2.add_lecturer(lecturer2)

# Добавление оценок студентам и лекторам
student1.add_grade(4)
student1.add_grade(5)
student2.add_grade(3)
student2.add_grade(4)
lecturer1.add_grade(4)
lecturer1.add_grade(4)
lecturer2.add_grade(5)
lecturer2.add_grade(5)

# Вызов методов и печать результатов
print(f"Студент {student1.name}: средняя оценка за домашние задания — {student1.calculate_avg_grade()}")
print(f"Студент {student2.name}: средняя оценка за домашние задания — {student2.calculate_avg_grade()}")
print()
print(f"Лектор {lecturer1.name}: средняя оценка за лекции — {lecturer1.calculate_avg_grade()}")
print(f"Лектор {lecturer2.name}: средняя оценка за лекции — {lecturer2.calculate_avg_grade()}")
print()
print(f"Средняя оценка за домашние задания по курсу {course1.name}: {calculate_avg_homework_grade(course1.students, course1.name)}")
print(f"Средняя оценка за домашние задания по курсу {course2.name}: {calculate_avg_homework_grade(course2.students, course2.name)}")
print(f"Средняя оценка за лекции по курсу {course1.name}: {calculate_avg_lecture_grade(course1.lecturers, course1.name)}")
print(f"Средняя оценка за лекции по курсу {course2.name}: {calculate_avg_lecture_grade(course2.lecturers, course2.name)}")