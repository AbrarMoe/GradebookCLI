object Authentication {
    data class User(val password: String, val role: String)

    fun authenticate(users: Map<String, User>): Pair<String?, String?> {
        print("Enter username: ")
        val username = readlnOrNull()?.trim() ?: ""
        print("Enter password: ")
        val password = readlnOrNull()?.trim() ?: ""

        val user = users[username]
        return if (user != null && user.password == password) {
            println("Welcome, $username!")
            Pair(username, user.role)
        } else {
            println("Invalid credentials. Please try again.")
            Pair(null, null)
        }
    }
}