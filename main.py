class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self._average_rating = sum(self.grades) / len(self.grades)

    def rate_Lecturer(self, lecturer, course, grade_Lecturer):
        if isinstance(lecturer, Lecturer) and course in self.courses_attached and course in lecturer.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade_Lecturer]
            else:
                lecturer.grades[course] = [grade_Lecturer]
        else:
            return 'Ошибка'

    def __str__(self):
        print(f"Имя: {self.name} "
                f"Фамилия: {self.surname}"
                f"Средняя оценка за домашние задания: {self._average_rating}"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}"
                f"Завершенные курсы: {', '.join(self.finished_courses)}")
    def __lt__(self, student):
        min_rating = self._average_rating
        return self._average_rating < min_rating

    def stud_vs_stud(self, student, course):
        for grade in student.grades:
            self.grades[course] += student.grades[course]
            self.grades[course] /= len(student.grades[course])
        return self.grades[course]


    def average_rating_stud(self,student, course):
        student = [student]
        for grade in student.grades:
            self.grades[course] += student.grades[course]
            self.grades[course] /= len(student.grades[course])
        return self.grades[course]

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_Lecturer = {}
        self._average_rating = sum(self.grades_Lecturer) / len(self.grades_Lecturer)


    def __str__(self):
        print(f"Имя: {self.name} "
                f"Фамилия: {self.surname}"
                f"Средняя оценка за лекции: {self._average_rating}")

    def __lt__(self, lecturer):
        min_rating = self._average_rating
        return self._average_rating < min_rating

    def lec_vs_lec(self, lecturer, course):
        for grade in lecturer.grades:
            self.grades[course] += lecturer.grades[course]
            self.grades[course] /= len(lecturer.grades[course])
        return self.grades[course]

    def average_rating_lec(self, lecturer, course):
        lecturer = [lecturer]
        for grade in lecturer.grades:
            self.grades[course] += lecturer.grades[course]
            self.grades[course] /= len(lecturer.grades[course])
        return self.grades[course]

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        print(f"Имя: {self.name} "
                f"Фамилия: {self.surname}")


    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

print(best_student.grades)


Student1 = Student('Natliya','Natalina','woman')
Student1.courses_in_progress = ['Python' , 'Git']
Student1.finished_courses = ['Java']
Student1.rate_Lecturer(Lecturer, 'Python', 10)
Student1.stud_vs_stud(Student, 'Python')

Student2 = Student('Ivan','Ivanov','man')
Student2.courses_in_progress = ['Python']
Student2.finished_courses = ['Java']
Student2.rate_Lecturer(Lecturer, 'Python', 9)
Student2.stud_vs_stud(Student1, 'Python')

Mentor1 = Mentor('Oleg', 'Olegov')
Mentor1.courses_attached = ['Python']

Mentor2 = Mentor('Alex', 'Alexeiev')
Mentor2.courses_attached = ['Python']

Lecturer1 = Lecturer('Oleg', 'Olegov')
Lecturer1.courses_attached = ['Python']
Lecturer1.lec_vs_lec(Lecturer, 'Python')

Lecturer2 = Lecturer('Alex', 'Alexeiev')
Lecturer2.courses_attached = ['Python']
Lecturer2.lec_vs_lec(Lecturer1, 'Python')

Reviewer1 = Reviewer('Petr', 'Petrov')
Reviewer1.courses_attached = ['Python']
Reviewer1.rate_hw(Student1, 'Python', 10)
Reviewer1.rate_hw(Student2, 'Python', 10)

Reviewer2 = Reviewer('Sidor', 'Sidorov')
Reviewer2.courses_attached = ['Python']
Reviewer2.rate_hw(Student1, 'Python', 9)
Reviewer2.rate_hw(Student2, 'Python', 9)
