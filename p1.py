import random

current_ids = []
current_users = {}


@staticmethod
def create_id():
    while True:
        id = random.randint(10000000, 99999999)
        if id not in current_ids:
            current_ids.append(id)
            return id


class User:
    def __init__(self):
        self.id = create_id()

    def create_account(self, username, password):
        if username not in current_users:
            Member(self.id, username, password)
        else:
            print(f"{username} ya está en uso")


class Guest(User):
    def __init__(self, id: int):
        super().__init__(id)
        self.name = f"Guest{id}"


class Member(User):
    def __init__(self, id: int, name: str, password: str):
        super().__init__(id)
        self.name = name
        self.password = password
        self.login_status = False

    def login(self, username, password):
        if username in current_users and current_users[username] == password:
            self.login_status = True

    def logout(self):
        if self.login_status:
            not self.login_status
