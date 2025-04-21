import kotlinx.serialization.Serializable
import kotlinx.serialization.json.Json
import java.io.File

@Serializable
data class StudentRecord(val name: String, val grades: List<Double>)

fun main() {
    println("=== Student Grade Management System ===")
    
    val users = mapOf(
        "admin" to Authentication.User("adminpass", "admin"),
        "student101" to Authentication.User("studpass", "student"),
        "student102" to Authentication.User("studpass102", "student"),
        "student103" to Authentication.User("studpass103", "student"),
        "student104" to Authentication.User("studpass104", "student")
    )

    val (username, role) = Authentication.authenticate(users)
    if (username == null || role == null) return

    when (role) {
        "admin" -> adminMenu()
        "student" -> studentMenu(username)
        else -> println("Unknown role encountered.")
    }
}

private fun adminMenu() {
    while (true) {
        println("\n*** Admin Menu ***")
        println("1. Add Student Record")
        println("2. Update Student Record")
        println("3. Delete Student Record")
        println("4. View Statistics")
        println("5. Sort Students")
        println("6. Exit")
        print("Enter your choice (1-6): ")
        
        when (readlnOrNull()?.trim()) {
            "1" -> {
                print("Enter Student ID: ")
                val studentId = readlnOrNull()?.trim() ?: ""
                print("Enter Student Name: ")
                val name = readlnOrNull()?.trim() ?: ""
                
                val numSubjects = try {
                    print("Enter number of subjects: ")
                    readlnOrNull()?.trim()?.toInt() ?: 0
                } catch (e: NumberFormatException) {
                    println("Invalid number!")
                    continue
                }
                
                print("Enter grades separated by commas (e.g., 85,78,92,88): ")
                val gradesInput = readlnOrNull()?.trim() ?: ""
                val grades = gradesInput.split(",")
                    .mapNotNull { it.trim().toDoubleOrNull() }
                
                if (grades.size != numSubjects) {
                    println("The number of grades does not match the number of subjects!")
                    continue
                }
                
                StudentManager.addStudentRecord(studentId, name, grades)
            }
            
            "2" -> {
                print("Enter Student ID to update: ")
                val studentId = readlnOrNull()?.trim() ?: ""
                val rec = StudentManager.getStudentRecord(studentId)
                
                if (rec == null) {
                    println("Student not found!")
                    continue
                }
                
                println("Current grades for ${rec.name}: ${rec.grades}")
                print("Enter new grades separated by commas: ")
                val newGradesInput = readlnOrNull()?.trim() ?: ""
                val newGrades = newGradesInput.split(",")
                    .mapNotNull { it.trim().toDoubleOrNull() }
                
                StudentManager.updateStudentRecord(studentId, newGrades)
            }
            
            "3" -> {
                print("Enter Student ID to delete: ")
                val studentId = readlnOrNull()?.trim() ?: ""
                StudentManager.deleteStudentRecord(studentId)
            }
            
            "4" -> {
                Statistics.generateStatistics(StudentManager.loadAllRecords())
            }
            
            "5" -> {
                val records = StudentManager.loadAllRecords()
                if (records.isEmpty()) {
                    println("No records to sort.")
                    continue
                }
                
                println("\nSort by:")
                println("1. GPA (highest first)")
                println("2. Name (alphabetical)")
                print("Enter your choice (1-2): ")
                
                when (readlnOrNull()?.trim()) {
                    "1" -> {
                        val sorted = Statistics.sortStudents(records, "gpa")
                        printSortedStudents(sorted)
                    }
                    "2" -> {
                        val sorted = Statistics.sortStudents(records, "name")
                        printSortedStudents(sorted)
                    }
                    else -> println("Invalid choice.")
                }
            }
            
            "6" -> {
                println("Exiting Admin Menu.")
                return
            }
            
            else -> println("Invalid choice. Try again.")
        }
    }
}

private fun printSortedStudents(students: List<Triple<String, String, Double>>) {
    println("\n=== Sorted Students ===")
    students.forEach {
        println("ID: ${it.first}, Name: ${it.second}, GPA: ${"%.2f".format(it.third)}")
    }
}

private fun studentMenu(username: String) {
    val rec = StudentManager.getStudentRecord(username)
    if (rec != null) {
        println("\n*** Student Record for ${rec.name} (ID: $username) ***")
        println("Grades: ${rec.grades}")
        val gpa = Statistics.computeGPA(rec.grades)
        println("GPA: ${"%.2f".format(gpa)}")
    } else {
        println("Student record not found.")
    }
}


