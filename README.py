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
        __class__.all_students.append(self)

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lec(self, lectur, course, grade):
        if isinstance(lectur, Lecturer) and course in lectur.courses_attached and course in self.courses_in_progress:
            if 1 <= float(grade) <= 10 and grade % 1 == 0:
                if course in lectur.grades:
                    lectur.grades[course] += [grade]
                else:
                    lectur.grades[course] = [grade]
            else:
                print('Пожалуйста, введите целое число от 1 до 10.')

    def __average(self):
        x = 0
        y = 0
        if len(self.grades) != 0:
            for i in self.grades:
                for j in self.grades[i]:
                    x += j
                    y += 1
            return x / y
        else:
            return 'У студента пока нет оценок за задания'

    def __lt__(self, other):
        if isinstance(other, Student) and isinstance(self, Student):
            return self.__average() < other.__average()

    def __str__(self):
        ex = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.__average()}\n'\
             f'Курсы в процессе изучения: {", ".join(self.courses_in_progress) }\n' \
             f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return ex


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    all_lecterers = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        __class__.all_lecterers.append(self)

    def __average(self):
        x = 0
        y = 0
        if len(self.grades) != 0:
            for i in self.grades:
                for j in self.grades[i]:
                    x += j
                    y += 1
            return x / y
        else:
            return 'У лектора пока нет оценок за лекции'

    def __str__(self):
        ex = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.__average()}'
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
some_student.courses_in_progress += ['Python']
some_student.finished_courses += ['Вводный модуль для студентов профессий PD и FPY']
some_student.finished_courses += ['Основы языка программирования Python']
some_student.finished_courses += ['GIT - система контроля версий']

other_student = Student('Артем', 'Кругляков', 'Мужчина')
other_student.courses_in_progress += ['Python']
other_student.courses_in_progress += ['Английский для IT-специалистов']
other_student.courses_in_progress += ['Python']

oleg_buligin = Lecturer('Олег', 'Булыгин')
oleg_buligin.courses_attached += ['Python']

nikita_blinov= Lecturer('Никита', 'Блинов')
nikita_blinov.courses_attached += ['Python']

dmitriy_losev = Reviewer('Дмитрий', 'Лосев')
dmitriy_losev.courses_attached += ['Python']

evgeniy_slow = Reviewer('Дмитрий', 'Медленный')
evgeniy_slow.courses_attached += ['Python']

dmitriy_losev.rate_hw(some_student, 'Python', 10)
dmitriy_losev.rate_hw(some_student, 'Python', 10)

dmitriy_losev.rate_hw(other_student, 'Python', 2)
dmitriy_losev.rate_hw(other_student, 'Python', 3)

some_student.rate_lec(oleg_buligin, 'Python', 10)
some_student.rate_lec(oleg_buligin, 'Python', 9)

some_student.rate_lec(nikita_blinov, 'Python', 9)
some_student.rate_lec(nikita_blinov, 'Python', 6)

x = 0
for _ in Student.all_students:
