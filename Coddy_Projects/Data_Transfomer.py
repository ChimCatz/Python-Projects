def transform_dataset(data):
    qualified_students = {}
    subject_summary = {}

    for record in data:
        student_id = record.get("student_id")
        grades = record.get("grades", [])
        subjects = record.get("subjects", [])

        # Only include students whose grades are all above 70
        if not grades or not all(grade > 70 for grade in grades):
            continue

        # Calculate average grade
        avg_grade = round(sum(grades) / len(grades), 2)
        qualified_students[student_id] = avg_grade

        # Count all subject occurrences (including duplicates)
        for subject in subjects:
            subject_summary[subject] = subject_summary.get(subject, 0) + 1

    return {
        "qualified_students": qualified_students,
        "subject_summary": subject_summary
    }
