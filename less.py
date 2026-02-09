# class Mark:
#     def __init__(self, student, subject, mark):
#         self.student = student
#         self.subject = subject
#         self.mark = mark
# class Journal:
#     def __init__(self, title):
#         self.title = title
#         self.students = []
#         self.subjects = []
#         self.marks = []
#     def add_students(self, students):
#         for student in students:
#             self.students.append(students)

#     def add_subjects(self, students):
#             for studen in studens:
#                 self.students.append(student)


class Pyramid:
    def __init__(self, max_h,):
        self.max_h = max_h
        self.bricks_count = 0

    def add_bricks(self, count):
        self.bricks_count += 1

    def is_done(self):
        return self.bricks_count >= ((self.max_h*(self.max_h+1))/2)

    def get_height(self):
        if self.bricks_count <= self.max_h:
            return 1
        else:
            virtual_bricks = self.bricks_count
            current_level = 1
            current_level_bricks_count = self.max_h
            while virtual_bricks > 0:
                virtual_bricks -= current_level_bricks_count
                current_level_bricks_count -= 1
                current_level += 1
            return current_level - 1

pyramid = Pyramid(5)
for i in range(10):
    pyramid.add_bricks(1)
    print(pyramid.get_height())