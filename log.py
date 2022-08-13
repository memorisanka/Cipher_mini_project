class User:
    def __init__(self):
        self.users_buffer = {}

    def add(self, usr: str, pw: str) -> None:
        self.users_buffer.update({usr: pw})

    def remove(self, user: str) -> None:
        self.users_buffer.pop(user, "User not found")

    def check(self, usr: str, pw: str) -> bool:
        if self.users_buffer[usr] == pw:
            return True

        return False
