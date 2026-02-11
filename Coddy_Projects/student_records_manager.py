student_records = {}

def add_student(name, age, courses):
    if name in student_records:
        print(f"Student '{name}' already exists.")
    else:
        student_records[name] = {}
        student_records[name]["age"] = age
        student_records[name]["grades"] = set()
        student_records[name]["courses"] = courses
        print(f"Student '{name}' added successfully.")

def add_grade(name, grade):
    if name not in student_records:
        print(f"Student '{name}' not found.")
    else:
        student_records[name]["grades"].add(grade)
        print(f"Grade {grade} added for student '{name}'.")

def is_enrolled(name, course):
    if name not in student_records:
        print(f"Student '{name}' not found.")
        return False
    else:
        if course in student_records[name]["courses"]:
            return True
        else:
            return False

def calculate_average_grade(name):
    if name not in student_records:
        print(f"Student '{name}' not found.")
        return None

    grades = student_records[name]["grades"]

    if len(grades) == 0:
        return 0

    total = 0
    for g in grades:
        total += g

    average = total / len(grades)
    return float(average)

def list_students_by_course(course):
    same_course = []

    for name, obj in student_records.items():
        if course in obj["courses"]:
            same_course.append(name)

    return same_course

def filter_top_students(threshold):
    top_students = []
    for student in student_records:
        if calculate_average_grade(student) > threshold:
            top_students.append(student)
    return top_students


#Add or replace bottom code
add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Math", "Biology"])
add_student("Diana", 23, ["Chemistry", "Physics"])
add_grade("Alice", 90)
add_grade("Alice", 85)
add_grade("Bob", 75)
add_grade("Diana", 95)
print(filter_top_students(80))  # Should return ["Alice", "Diana"]
print(filter_top_students(90))  # Should return ["Diana"]
print(filter_top_students(100))  # Should return an empty list
