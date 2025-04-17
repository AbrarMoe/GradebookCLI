# statistics.py

def compute_gpa(grades):
    """Compute GPA: sum of grades divided by the number of subjects."""
    if not grades:
        return 0
    return sum(grades) / len(grades)

def generate_statistics(records):
    """Generate and print summary statistics for all student records, including grade distribution."""
    if not records:
        print("No records found!")
        return

    stats_list = []
    grade_counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
    
    for student_id, rec in records.items():
        gpa = compute_gpa(rec["grades"])
        stats_list.append((student_id, rec["name"], gpa))
        
        # Categorize GPA into grades
        if gpa >= 90:
            grade_counts['A'] += 1
        elif gpa >= 80:
            grade_counts['B'] += 1
        elif gpa >= 70:
            grade_counts['C'] += 1
        elif gpa >= 60:
            grade_counts['D'] += 1
        else:
            grade_counts['F'] += 1

    # Calculate average, highest, and lowest GPA
    total_gpa = sum(gpa for _, _, gpa in stats_list)
    average_gpa = total_gpa / len(stats_list) if stats_list else 0
    highest = max(stats_list, key=lambda x: x[2], default=None)
    lowest = min(stats_list, key=lambda x: x[2], default=None)

    print("\n=== Class Statistics ===")
    print(f"Average GPA: {average_gpa:.2f}")
    if highest:
        print(f"Highest GPA: {highest[2]:.2f} (Student: {highest[1]}, ID: {highest[0]})")
    if lowest:
        print(f"Lowest GPA: {lowest[2]:.2f} (Student: {lowest[1]}, ID: {lowest[0]})")
    
    # Print grade distribution
    print("\n=== Grade Distribution ===")
    for grade, count in grade_counts.items():
        print(f"{grade}: {count} student(s)")

def sort_students(records, sort_by='gpa'):
    """Sort students by GPA (descending) or name (ascending). Returns a sorted list."""
    stats_list = []
    for student_id, rec in records.items():
        gpa = compute_gpa(rec["grades"])
        stats_list.append((student_id, rec["name"], gpa))
    
    if sort_by == 'name':
        return sorted(stats_list, key=lambda x: (x[1].lower(), x[0]))
    else:
        return sorted(stats_list, key=lambda x: (-x[2], x[0]))