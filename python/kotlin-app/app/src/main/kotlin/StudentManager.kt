import kotlinx.serialization.*
import kotlinx.serialization.json.*
import java.io.File


object StudentManager {
    private const val DATA_FILE = "src/main/resources/student_records.json"

    private fun loadRecords(): MutableMap<String, StudentRecord> {
        val file = File(DATA_FILE)
        return if (file.exists()) {
            Json.decodeFromString(file.readText())
        } else mutableMapOf()
    }

    private fun saveRecords(records: Map<String, StudentRecord>) {
        File(DATA_FILE).writeText(Json.encodeToString(records))
    }

    fun addStudentRecord(id: String, name: String, grades: List<Double>) {
        val records = loadRecords().toMutableMap()
        if (records.containsKey(id)) {
            println("Student record already exists!")
            return
        }
        records[id] = StudentRecord(name, grades)
        saveRecords(records)
        println("Student added successfully!")
    }

    fun getStudentRecord(id: String): StudentRecord? = loadRecords()[id]

    fun updateStudentRecord(id: String, newGrades: List<Double>) {
        val records = loadRecords().toMutableMap()
        records[id]?.let {
            records[id] = it.copy(grades = newGrades)
            saveRecords(records)
            println("Student record updated successfully!")
        } ?: println("Student not found!")
    }

    fun deleteStudentRecord(id: String) {
        val records = loadRecords().toMutableMap()
        if (records.remove(id) != null) {
            saveRecords(records)
            println("Student record deleted!")
        } else {
            println("Student record not found!")
        }
    }

    fun loadAllRecords(): Map<String, StudentRecord> = loadRecords()
}