# courses marks as input and then calculates average of all the courses .

num_courses = int(input("Enter the number of courses: "))
total_marks = 500

total_course_marks = 0

for i in range(num_courses):
    course_marks = int(input(f"Enter marks for course {i + 1}: "))
    total_course_marks += course_marks

average_marks = total_course_marks / num_courses

percentage = (total_course_marks / total_marks) * 100

print(f"Average Marks: {average_marks}")
print(f"Percentage: {percentage}%")
