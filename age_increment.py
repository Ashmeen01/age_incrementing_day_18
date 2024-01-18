# Assignment 1

# Question I
#  write a python notebook that takes student's age, 
# check the ones who are below 18 and increment them until the get to 18 years.


# Answer 1
# Function to increment age to 18
def increment_to_18(age):
    while age < 18:
        age += 1
    return age

# Function to process student ages
def process_student_ages(student_ages):
    updated_ages = [increment_to_18(age) for age in student_ages]
    return updated_ages

#  list of student ages
student_ages = [16, 19, 14, 22, 17, 20]

# Process and print the updated ages
updated_ages = process_student_ages(student_ages)
print(f'Original age: {student_ages}')
print(f'Updated age that increment by the system: {updated_ages}')
