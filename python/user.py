class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email

    def __repr__(self):
        return f"User(username={self.username}, name={self.name}, email={self.email})"

    def __str__(self):
        return self.__repr__()


class UserDatabase:
    def __init__(self):
        # dictionary for fast lookup (instead of list)
        self.users = {}

    def insert(self, user):
        """Insert a user (O(1))"""
        if user.username in self.users:
            raise ValueError("Username already exists!")
        self.users[user.username] = user

    def find(self, username):
        """Find a user by username (O(1))"""
        return self.users.get(username, None)

    def update(self, user):
        """Update user details (O(1))"""
        if user.username not in self.users:
            raise ValueError("User not found!")
        self.users[user.username] = user

    def delete(self, username):
        """Delete user (O(1))"""
        if username in self.users:
            del self.users[username]

    def list_all(self):
        """List all users"""
        return list(self.users.values())


# Example usage
if __name__ == "__main__":
    db = UserDatabase()

    # Insert users
    db.insert(User("u1", "Alice", "alice@example.com"))
    db.insert(User("u2", "Bob", "bob@example.com"))

    # Find user
    print(db.find("u1"))

    # Update user
    db.update(User("u1", "Alice Wonderland", "alice.w@example.com"))
    print(db.find("u1"))

    # Delete user
    db.delete("u2")
    print(db.list_all())
