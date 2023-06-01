class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Wrong"

    # def add_courses(self, course_name):
    #     self.finished_courses.append(course_name)

    def av_rating(self):
        sum_rating = 0
        len_rating = 0
        for course in self.grades.values():
            sum_rating += sum(course)
            len_rating += len(course)
        average_rating = round(sum_rating / len_rating, 2)
        return average_rating

    def av_rating_for_course(self, course):
        sum_rating = 0
        len_rating = 0
        for lesson in self.grades.keys():
            sum_rating += sum(self.grades[course])
            len_rating += len(self.grades[course])
        average_rating = round(sum_rating / len_rating, 2)
        return average_rating

    def __str__(self):
        res = f'Name: {self.name}\nSurname: {self.surname}\nAverage grade for homework tasks: {self.av_rating()}\nCourses in progress: {", ".join(self.courses_in_progress)}\nFinished courses: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Mentors and students don't compare")
            return
        return self.av_rating() < other.av_rating()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def av_rating(self):
        sum_rating = 0
        len_rating = 0
        for course in self.grades.values():
            sum_rating += sum(course)
            len_rating += sum(course)
        averang_rating = round(sum_rating / len_rating, 2)
        return averang_rating

    def av_rating_for_course(self, course):
        sum_rating = 0
        len_rating = 0
        for lesson in self.grades.keys():
            if lesson == course:
                sum_rating += sum(self.grades[course])
                len_rating += len(self.grades[course])
        average_rating = round(sum_rating / len_rating, 2)
        return average_rating

    def __str__(self):
        res = f"Name: {self.name}\nSurname: {self.surname}\nAverage grade for lectures: {self.av_rating()}"
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Mentors and students don't compare")
            return
        return self.av_rating() < other.av_rating()

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Wrong"
    def __str__(self):
        res = f"Name: {self.name} \nSurname: {self.surname}"
        return res

# Students
student_1 = Student("Harry", "Potter", "Male")
student_1.courses_in_progress += ["Python, Git"]
student_1.finished_courses += ["Introduction to Programming"]

student_2 = Student("Stephanie", "Miller", "Female")
student_2.courses_in_progress += ["Python, Git"]
student_2.finished_courses += ["Introduction to Programming"]

# Lecturers
lecturer_1 = Lecturer("Michael", "Smith")
lecturer_1.courses_attached += ["Python, Git"]

lecturer_2 = Lecturer("Emma", "Golden Mayer")
lecturer_2.courses_attached += ["Python, Git"]

# Reviewers
reviewer_1 = Reviewer("Jack", "Phobus")
reviewer_1.courses_attached += ["Python, Git"]

reviewer_2 = Reviewer("Guzel", "Aram")
reviewer_2.courses_attached += ["Python, Git"]

# Grades for students
reviewer_1.rate_hw(student_1, "Python, Git", 10)
reviewer_1.rate_hw(student_1, "Python, Git", 9)
reviewer_1.rate_hw(student_1, "Python, Git", 8)

reviewer_2.rate_hw(student_2, "Python, Git", 10)
reviewer_2.rate_hw(student_2, "Python, Git", 7)
reviewer_2.rate_hw(student_2, "Python, Git", 6)

# Grades for lecturers
student_1.rate_lw(lecturer_1, "Python, Git", 10)
student_1.rate_lw(lecturer_1, "Python, Git", 5)
student_1.rate_lw(lecturer_1, "Python, Git", 4)

student_2.rate_lw(lecturer_2, "Python, Git", 10)
student_2.rate_lw(lecturer_2, "Python, Git", 3)
student_2.rate_lw(lecturer_2, "Python, Git", 2)

student_list = [student_1, student_2]
lecturer_list = [lecturer_1, lecturer_2]
reviewer_list = [reviewer_1, reviewer_2]

def average_rating_for_course(course, student_list):
    sum_rating = 0
    quantity_rating = 0
    for stud in student_list:
        for course in stud.grades:
            stud_sum_rating = stud.av_rating_for_course(course)
            sum_rating += stud_sum_rating
            quantity_rating += 1
    average_rating = round(sum_rating / quantity_rating, 2)
    return average_rating


# print(average_rating_for_course("Python, Git", student_list))
# print(average_rating_for_course("Python, Git", lecturer_list))
print(student_1)
print(student_2)
print(lecturer_1)
print(lecturer_2)