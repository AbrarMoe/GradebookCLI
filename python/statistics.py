# statistics.py

def compute_gpa(grades):
    """Compute GPA: sum of grades divided by the number of subjects."""
    if not grades:
        return 0
    return sum(grades) / len(grades)

def generate_statistics(records):
    """Generate and print summary statistics for all student records."""
    if not records:
        print("No records found!")
        return

    stats_list = []
    for student_id, rec in records.items():
        gpa = compute_gpa(rec["grades"])
        stats_list.append((student_id, rec["name"], gpa))

    total_gpa = sum(gpa for _, _, gpa in stats_list)
    average_gpa = total_gpa / len(stats_list)
    highest = max(stats_list, key=lambda x: x[2])
    lowest = min(stats_list, key=lambda x: x[2])

    print("\n=== Class Statistics ===")
    print(f"Average GPA: {average_gpa:.2f}")
    print(f"Highest GPA: {highest[2]:.2f} (Student: {highest[1]}, ID: {highest[0]})")
    print(f"Lowest GPA: {lowest[2]:.2f} (Student: {lowest[1]}, ID: {lowest[0]})")
