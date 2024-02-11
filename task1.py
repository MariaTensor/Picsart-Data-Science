import numpy as np
import matplotlib.pyplot as plt


student_grades = {
    "Alice": 88,
    "Bob": 76,
    "Charlie": 90,
    "Diana": 85,
    "Evan": 92,
    "Fiona": 79,
    "George": 95
}
# The average grade
mean_grade = np.mean(list(student_grades.values()))
print(mean_grade)
# The maximum grade
max_grade = np.max(list(student_grades.values()))
max_grade_name = {i for i in student_grades if student_grades[i] == max_grade}
print(max_grade, max_grade_name)
# The minimum grade
min_grade = np.min(list(student_grades.values()))
min_grade_name = {i for i in student_grades if student_grades[i] == min_grade}
print(min_grade, min_grade_name)
# Grade Distribution
PASS = []
FAIL = []
passed_students = []
failed_students = []

for i, j in student_grades.items():
    if j < 75:
        FAIL.append(j)
        failed_students.append(i)
    else:
        PASS.append(j)
        passed_students.append(i)

# Improvement Suggestions
for i, j in student_grades.items():
    if j < 85:
        print(f"{i} you will better to attend additional classes")


# Visual Representation
names = list(student_grades.keys())
grades = list(student_grades.values())
plt.bar(range(len(student_grades)), grades, tick_label=names)
plt.xlabel('Students')
plt.ylabel('Grades')
plt.title('Student Grades')
plt.show()

symbol = '='
for student, grade in student_grades.items():
    print(f"{student}: {symbol * grade}")
