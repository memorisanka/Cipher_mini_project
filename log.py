class User:
    def __init__(self):
        self.users_buffer = {}

    def add(self, user: str, password: str) -> None:
        self.users_buffer.update({user: password})

    def remove(self, user: str, password: str) -> None:
        self.users_buffer.remove[user]

