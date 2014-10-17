class Student:
  def __init__(self, name):
    self.name = name
    self.attend = 0
    self.grades = []

  def addGrade(self, grade):
    self.grades.append(grade)


