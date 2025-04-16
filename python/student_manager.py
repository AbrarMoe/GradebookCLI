import json
import os

DATA_FILE = "student_records.json"

def load_student_records():
    """Load student records from a JSON file. Returns a dictionary."""
    if not os.path.exists(DATA_FILE):
        return {}  # If the file does not exist, return an empty dictionary.
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_student_records(records):
    """Save the given records dictionary to a JSON file."""
    # Create the directory for DATA_FILE if it doesn't exist.
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w") as file:
        json.dump(records, file, indent=4)

def add_student_record(student_id, name, grades):
    """Add a new student record if one with the same id doesn't already exist."""
    records = load_student_records()
    if student_id in records:
        print("Student record already exists!")
        return
    records[student_id] = {
        "name": name,
        "grades": grades
    }
    save_student_records(records)
    print("Student added successfully!")

def get_student_record(student_id):
    """Retrieve a student record by student_id."""
    records = load_student_records()
    return records.get(student_id)

def update_student_record(student_id, new_grades):
    """Update the grades of an existing student record."""
    records = load_student_records()
    if student_id not in records:
        print("Student not found!")
        return
    records[student_id]["grades"] = new_grades
    save_student_records(records)
    print("Student record updated successfully!")

def delete_student_record(student_id):
    """Delete a student record."""
    records = load_student_records()
    if student_id in records:
        del records[student_id]
        save_student_records(records)
        print("Student record deleted!")
    else:
        print("Student record not found!")
