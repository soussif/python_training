from useful_tools import Student
from useful_tools import SpecialStudent


student1 = Student("Faek", "IT", 5)
student2 = Student("Mauricio", "Accounting", 2.8)
print(student1.gpa)
print("student 1 is on honor: " + str(student1.on_honor_roll()))
print("student 2 is on honor: " + str(student2.on_honor_roll()))
student3 = SpecialStudent("Hubert", "Art", 2.5)
print(student3.name)
print(student3.on_honor_roll())
print(student3.special_student())
