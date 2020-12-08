class School:
    def __init__(self):
        self.students = {}

    def add_student(self, name, grade):
        self.students[name]= grade

    def roster(self, grade_number=0):
        results = []
        if len(self.students) < 0:
          return []
        elif grade_number == 0:
          for i in self.grade(grade_number):
            results.append(i[0])
          print(results)
        else:
          print(sorted(self.grade(grade_number)))


    def grade(self, grade_number):
      grade_students = {}
      if grade_number >= 1:
        for student in self.students.items():
          if student[1] == grade_number:
            grade_students[student[0]] = student[1]
        return grade_students
      else:
        grade_students = sorted(self.students.items(), key=lambda x: x[1])
        return grade_students
