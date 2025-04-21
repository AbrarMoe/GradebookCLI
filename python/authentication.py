def authenticate(users):
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    
    user = users.get(username)
    if user and user["password"] == password:
        print(f"Welcome, {username}!")
        return username, user["role"]
    else:
        print("Invalid credentials. Please try again.")
        return None, None

if __name__ == "__main__":
    test_users = {
        "admin": {"password": "adminpass", "role": "admin"},
        "student101": {"password": "studpass", "role": "student"}
    }
    authenticate(test_users)
