class User:
    def __init__(self):
        self.users_buffer = {}

    def add(self, user: str, password: str) -> None:
        self.users_buffer.update({user: password})

    def remove(self, user: str) -> None:
        self.users_buffer.pop(user, "User not found")

    def check(self, user: str, password: str):
        if self.users_buffer[user] == password:
            return True
        return False
