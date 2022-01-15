student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# print(student_heights)


number_of_students = 0
total_heights = 0

for student in student_heights:
  number_of_students +=1

print('Number of students:', number_of_students)

for height in student_heights:
  total_heights = total_heights + height

print('Total hights of all students is:', total_heights)

average_height = total_heights / number_of_students

print(f'Average height rounded to the nearest whole number = {average_height:.2f}')



