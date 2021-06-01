student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇

for key in student_scores:
  if student_scores[key] > 90:
    value = "Outstanding"
  elif student_scores[key] > 80:
    value = "Exceeds Expectations"
  elif student_scores[key] > 70:
    value = "Acceptable"
  else:
    value = "Fail" 
  student_grades[key] = value

    

# 🚨 Don't change the code below 👇
print(student_grades)





