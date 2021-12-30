from random import randint

class Student:
  name = "Unknown"
  surname = "Unknown"
  recordBookNumber = 0
  grades = []
  avgGrade = 0

  def __init__(self, name, surname, recordBookNumber, grades):
    if (len(grades) == 5):
      self.name = name
      self.surname = surname
      self.recordBookNumber = recordBookNumber
      self.grades = grades
      self.avgGrade = self.FindAverageScore()
    else:
      print("[ERROR] Grades should be 5!")

  def SetName(self, name):
    self.name = name
  def SetSurname(self, surname):
    self.surname = surname
  def SetRecordBookNumber(self, recordBookNumber):
    self.recordBookNumber = recordBookNumber
  def SetGrades(self, grades):
    self.grades = grades
  def SetAvgGrade(self):
    if len(grades) != 0:
      self.avgGrade = self.FindAverageScore()

  def GetName(self):
    return self.name
  def GetSurname(self):
    return self.surname
  def GetRecordBookNumber:
    return self.recordBookNumber
  def GetGrades(self):
    return self.grades
  def GetAvgGrade(self):
    return self.avgGrade

  def FindAverageScore(self):
    summa = 0
    count = 0

    for grade in grades:
      count += 1
      summa += grade

    return summa / count

  def ShowInfo(self):
    print("[STUDENT] Name = %s" % self.name)
    print("[STUDENT] Surname = %s" % self.surname)
    print("[STUDENT] Record book number = %s" % self.recordBookNumber)
    print("[STUDENT] Name = %s" % " ".join(str(i) for i in self.grades))


class Group:
  students = []

  def __init__(self, students):
    self.students = students

  def SetStudents(self, students):
    self.students = students

  def GetStudents(self):
    return self.students

  def AddStudent(self, student):
    if len(self.students) <= 20:
      self.students.append(student)
    else:
      print("[ERROR] There are 20 students! You can't add more!")

  def FindFiveBestAverageStudents(self):
    students.sort(key=lambda x: x.avgGrade, reverse=True)
    bestFiveStudents = students[:5]

    return bestFiveStudents

  def OutputFiveBestAverageStudents(self):
    bestFiveStudents = self.FindFiveBestAverageStudents()

    for bestStudent in bestFiveStudents:
      bestStudent.ShowInfo()
      print("\n")


if __name__ == "__main__":

  while(True):
    studentQuantity = int(input("[ENTER] Enter quantity of students: "))
    if studentQuantity >= 20:
      print("[ERROR] You can not set more than 20 students! Please repier your entering again :(")
      continue

    break

  students = []
  for i in range(studentQuantity):
    studentName = "StudentName%s" % i
    studentSurname = "StudentSurname%s" % i
    recordBookNumber = i
    grades = [randint(1, 5) for i in range(5)]
    student = Student(studentName, studentSurname, recordBookNumber, grades)
    students.append(student)

  print("[PROGRAM] Students were created!")
  print("\n")

  group = Group(students)

  group.OutputFiveBestAverageStudents()