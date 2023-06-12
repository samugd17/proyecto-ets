import re
from tablestars import User, Guest, Inventory, Member, current_users


class TestUser:
    user1 = User()
    guest1 = Guest()
    member1 = user1.create_account('peste','actuarconcriterio')
    inv1 = Inventory('peste')

    def test_build_user(self):
        assert 10000000 <= self.user1.id <= 99999999
        assert isinstance(self.user1, User)

    def test_build_guest(self):
        regex = r'Guest\d{8}'
        assert re.fullmatch(regex, self.guest1.username) is not None
        assert isinstance(self.guest1, Guest)

    def test_create_account(self):
        assert current_users['peste'] == 'actuarconcriterio'
        assert isinstance(self.member1, Member)

    def test_create_account_with_taken_username(self):
        self.user1.create_account('peste','1234')
        assert current_users['peste'] == 'actuarconcriterio'

    def test_member_login(self):
        self.member1.login(self.member1.username, self.member1.password)
        assert self.member1.login_status == True

    def test_member_logout(self):
        self.member1.login(self.member1.username, self.member1.password)
        self.member1.logout()
        assert self.member1.login_status == False

    def test_member_logout_when_alerady_logged_out(self):
        self.member1.logout()
        assert self.member1.login_status == False

    def test_build_inventory(self):
        assert self.inv1.username == 'peste'
        assert self.inv1.items == []

    def test_add_item(self):
        self.inv1.add_item('dado', 'cubiliete')
        assert self.inv1.items == ['dado', 'cubiliete']

    def test_remove_item(self):
        self.inv1.remove_item('dado')
        assert self.inv1.items == ['cubiliete']