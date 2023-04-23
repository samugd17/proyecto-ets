import random

current_users = {}


@staticmethod
def create_guest_name():
    while True:
        id = random.randint(10000000, 99999999)
        if id not in current_users:
            guest_name = f"Guest{id}"
            current_users[guest_name]
            return guest_name


class User:
    def add_guest(self):
        Guest()

    def create_account(self, username, password):
        if username not in current_users:
            if self.username:
                current_users.pop(self.username)
            Member(username, password)
            current_users[username] = password
        else:
            print(f"{username} ya está en uso")


class Guest(User):
    def __init__(self):
        self.username = create_guest_name()


class Member(User):
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password
        self.login_status = False

    def login(self, username: str, password: str) -> None:
        if username in current_users and current_users[username] == password:
            self.login_status = True

    def logout(self) -> None:
        if self.login_status:
            not self.login_status


class Inventory:
    def __init__(self, username: str):
        self.username = username
        self.items = []

    def get_item(self, item: str):
        pass

    def add_item(self, *items: str) -> None:
        for item in items:
            self.items.append(item)

    def remove_item(self, item: str) -> None:
        self.items.remove(item)
