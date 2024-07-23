# Write a program that converts their scores to grades.
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

# Create an empty dictionary called student_grades.
student_grades = {}

# Write a code to add the grades to student_grades.
for key in student_scores:
  score = student_scores[key]
  if score > 90:
    student_grades[key] = "Outstanding"
  elif score > 80:
    student_grades[key] = "Exceeds Expectations"
  elif score > 70:
    student_grades[key] = "Acceptable"
  else:
    student_grades[key] = "Fail"

print(student_grades)