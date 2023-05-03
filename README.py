import self as self


class Student:

    all_students = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.__class__.all_students.append(self)

    def cours_in_progress(self, course_name):
        self.courses_in_progress.append(course_name.title())

    def finish_courses(self, course_name):
        self.finished_courses.append(course_name.title())

    def rate_lec(self, lectur, course, grade):
        if isinstance(lectur, Lecturer) and course in lectur.courses_attached and course in self.courses_in_progress:
            if 1 <= grade <= 10 and grade % 1 == 0:
                if course in lectur.grades:
                    lectur.grades[course.title()] += [grade]
                else:
                    lectur.grades[course.title()] = [grade]
            else:
                print('Пожалуйста, введите целое число от 1 до 10.')

    def __average(self):
        _ = 0
        z = 0
        if len(self.grades) != 0:
            for i in self.grades:
                for j in self.grades[i]:
                    _ += j
                z += len(self.grades[i])
        else:
            return 'У студента пока нет оценок за лекции'
        return _ / z

    def __lt__(self, other):
        if isinstance(other, Student) and isinstance(self, Student):
            return self.__average() < other.__average()

    def __str__(self):
        ex = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: ' \
             f'{self.__average()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
             f'Завершенные курсы: {", ".join(self.finished_courses) if len(self.finished_courses) else "Студен пока не завершил ни одного курса."}'
        return ex


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    all_lecturers = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.__class__.all_lecturers.append(self)

    def __average(self):
        _ = 0
        z = 0
        if len(self.grades) != 0:
            for i in self.grades:
                for j in self.grades[i]:
                    _ += j
                z += len(self.grades[i])
        else:
            return 'У лектора пока нет оценок за лекции'
        return _ / z

    def __str__(self):
        ex = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {round(self.__average(), 2)}'
        return ex

    def __lt__(self, other):
        if isinstance(other, Lecturer) and isinstance(self, Lecturer):
            return self.__average() < other.__average()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        ex = f'Имя: {self.name}\nФамилия: {self.surname}'
        return ex


some_student = Student('Семен', 'Клюев', 'Мужчина')

some_student.courses_in_progress += ['ООП и работа с API']
some_student.courses_in_progress += ['Английский для IT-специалистов']
some_student.cours_in_progress('Python')
some_student.finished_courses += ['Вводный модуль для студентов профессий PD и FPY']
some_student.finished_courses += ['Основы языка программирования Python']
some_student.finish_courses('GIT - система контроля версий')

other_student = Student('Артем', 'Кругляков', 'Мужчина')
other_student.cours_in_progress('Python')
other_student.cours_in_progress('Английский для IT-специалистов')

oleg_buligin = Lecturer('Олег', 'Булыгин')
oleg_buligin.courses_attached += ['Python']

nikita_suslov = Lecturer('Никита', 'Суслов')
nikita_suslov.courses_attached += ['Python']


dmitriy_losev = Reviewer('Дмитрий', 'Лосев')
dmitriy_losev.courses_attached += ['Python']
dmitriy_losev.courses_attached += ['ООП и работа с API']

dmitriy_losev.rate_hw(some_student, 'Python', 10)
dmitriy_losev.rate_hw(some_student, 'Python', 3)
dmitriy_losev.rate_hw(some_student, 'Python', 10)
dmitriy_losev.rate_hw(some_student, 'Python', 8)
dmitriy_losev.rate_hw(some_student, 'Python', 8)
dmitriy_losev.rate_hw(some_student, 'Python', 10)
dmitriy_losev.rate_hw(some_student, 'ООП и работа с API', 5)
dmitriy_losev.rate_hw(some_student, 'ООП и работа с API', 7)
dmitriy_losev.rate_hw(some_student, 'ООП и работа с API', 2)
dmitriy_losev.rate_hw(some_student, 'ООП и работа с API', 5)
dmitriy_losev.rate_hw(other_student, 'Python', 2)
dmitriy_losev.rate_hw(other_student, 'Python', 3)

some_student.rate_lec(oleg_buligin, 'Python', 10)
some_student.rate_lec(oleg_buligin, 'Python', 8)
some_student.rate_lec(oleg_buligin, 'Python', 4)
some_student.rate_lec(oleg_buligin, 'Python', 5)
some_student.rate_lec(oleg_buligin, 'Python', 3)
some_student.rate_lec(nikita_suslov, 'Python', 3)
some_student.rate_lec(nikita_suslov, 'Python', 8)
some_student.rate_lec(nikita_suslov, 'Python', 4)
some_student.rate_lec(nikita_suslov, 'Python', 5)
some_student.rate_lec(oleg_buligin, 'ООП и работа с API', 9)
some_student.rate_lec(oleg_buligin, 'ООП и работа с API', 10)
some_student.rate_lec(oleg_buligin, 'ООП и работа с API', 9)
some_student.rate_lec(oleg_buligin, 'ООП и работа с API', 10)
some_student.rate_lec(oleg_buligin, 'ООП и работа с API', 5)


def all_grades_students(list_student, course_name):
    x = 0
    y = 0
    for _ in list_student:
        if course_name.title() in _.grades:
            for j in _.grades[course_name.title()]:
                x += j
                y += 1
        else:
            return 'У студентов пока нет оценок за данный курс'
        return f'Средняя оценка всех студентов курса {course_name} = {round(x/y, 2)}'


print(all_grades_students(Student.all_students, 'python'))
print()


def all_grades_lecturers(list_lecterurs, course_name):
    x = 0
    y = 0
    for _ in list_lecterurs:
        if course_name.title() in _.grades:
            for j in _.grades[course_name.title()]:
                x += j
                y += 1
        else:
            return 'У лекторов пока нет оценок за данный курс'
        return f'Средняя оценка всех лекторов курса {course_name} = {x / y}'


print(all_grades_lecturers(Lecturer.all_lecturers, 'Python'))
print()
print(some_student)
print()
print(oleg_buligin)
print()
print(dmitriy_losev)
print()
print(oleg_buligin > nikita_suslov)