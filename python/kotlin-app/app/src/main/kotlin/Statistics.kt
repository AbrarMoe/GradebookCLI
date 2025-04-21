object Statistics {
    fun computeGPA(grades: List<Double>): Double {
        return if (grades.isEmpty()) 0.0 else grades.average()
    }

    fun generateStatistics(records: Map<String, StudentRecord>) {
        if (records.isEmpty()) {
            println("No records found!")
            return
        }

        val stats = records.map { (id, rec) ->
            Triple(id, rec.name, computeGPA(rec.grades))
        }

        val averageGPA = stats.map { it.third }.average()
        val highest = stats.maxByOrNull { it.third }
        val lowest = stats.minByOrNull { it.third }

        val gradeCounts = mutableMapOf(
            'A' to 0, 'B' to 0, 'C' to 0, 'D' to 0, 'F' to 0
        )

        stats.forEach { (_, _, gpa) ->
            when {
                gpa >= 90 -> gradeCounts['A'] = gradeCounts['A']!! + 1
                gpa >= 80 -> gradeCounts['B'] = gradeCounts['B']!! + 1
                gpa >= 70 -> gradeCounts['C'] = gradeCounts['C']!! + 1
                gpa >= 60 -> gradeCounts['D'] = gradeCounts['D']!! + 1
                else -> gradeCounts['F'] = gradeCounts['F']!! + 1
            }
        }

        println("\n=== Class Statistics ===")
        println("Average GPA: ${"%.2f".format(averageGPA)}")
        highest?.let {
            println("Highest GPA: ${"%.2f".format(it.third)} (Student: ${it.second}, ID: ${it.first})")
        }
        lowest?.let {
            println("Lowest GPA: ${"%.2f".format(it.third)} (Student: ${it.second}, ID: ${it.first})")
        }

        println("\n=== Grade Distribution ===")
        gradeCounts.forEach { (grade, count) ->
            println("$grade: $count student(s)")
        }
    }

    fun sortStudents(records: Map<String, StudentRecord>, sortBy: String): List<Triple<String, String, Double>> {
        val stats = records.map { (id, rec) ->
            Triple(id, rec.name, computeGPA(rec.grades))
        }

        return when (sortBy) {
            "name" -> stats.sortedWith(compareBy({ it.second.lowercase() }, { it.first }))
            else -> stats.sortedWith(compareByDescending<Triple<String, String, Double>> { it.third }.thenBy { it.first })
        }
    }
}