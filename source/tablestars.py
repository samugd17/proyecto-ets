from __future__ import annotations
import random
import re

current_users = {}


@staticmethod
def create_guest_name():
    while True:
        id = random.randint(10000000, 99999999)
        if id not in current_users:
            guest_name = f"Guest{id}"
            current_users[guest_name] = 'placeholder'
            return guest_name

class User:
    def __init__(self):
        self.id = random.randint(10000000, 99999999)

    def create_account(self, username, password):
        if username not in current_users:
            current_users[username] = password
            return Member(username, password)
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
        self.friends = []

    def login(self, username: str, password: str) -> None:
        if username in current_users and current_users[username] == password:
            self.login_status = True

    def logout(self) -> None:
        if self.login_status:
            self.login_status = False

    def manage_friend_request(self, other: Member):
        regex = r'\w+[1-9]{1}'
        if re.fullmatch(regex, other.username) is None:
            self.friends.append(other.username)
            return 'Successfully accepted'
        else:
            return 'Successfully declined'


    def send_friend_request(self, other: Member):
        if other.manage_friend_request(self) == 'Successfully accepted':
            self.friends.append(other.username)
        else:
            return 'Declined'
        
    def remove_friend(self, other: Member):
        if other.username in self.friends:
            self.friends.remove(other.username)
            other.friends.remove(self.username)
            return 'Successfully removed'
        else:
            return f"You're not friends with {other.username}"

class Inventory:
    def __init__(self, username: str):
        self.username = username
        self.items = []

    def get_item(self, item: str):
        return item

    def add_item(self, *items: str) -> None:
        for item in items:
            self.items.append(item)

    def remove_item(self, item: str) -> None:
        self.items.remove(item)

def suma(n1, n2):
    if isinstance(n1, int) and isinstance(n2, int):
        return n1 + n2
