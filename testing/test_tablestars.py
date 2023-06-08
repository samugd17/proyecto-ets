import pytest
from tablestars import *
import re


user1 = User()
guest1 = Guest()
member1 = user1.create_account('peste','actuarconcriterio')
member2 = user1.create_account('welles','actuar')
member3 = user1.create_account('gdamn3','concriterio')
inv1 = Inventory('peste')

def test_build_user():
    assert 10000000 <= user1.id <= 99999999
    assert isinstance(user1, User)

def test_build_guest():
    regex = r'Guest\d{8}'
    assert re.fullmatch(regex, guest1.username) is not None
    assert isinstance(guest1, Guest)

def test_create_account():
    assert current_users['peste'] == 'actuarconcriterio'
    assert isinstance(member1, Member)

def test_create_account_with_taken_username():
    user1.create_account('peste','1234')
    assert current_users['peste'] == 'actuarconcriterio'

def test_member_login():
    member1.login(member1.username, member1.password)
    assert member1.login_status == True

def test_member_logout():
    member1.login(member1.username, member1.password)
    member1.logout()
    assert member1.login_status == False

def test_member_logout_when_alerady_logged_out():
    member1.logout()
    assert member1.login_status == False

def test_accept_friend_request():
    member2.send_friend_request(member1)
    assert member1.username in member2.friends
    assert member2.username in member1.friends

def test_decline_friend_request():
    member3.send_friend_request(member1)
    assert member1.username not in member3.friends
    assert member3.username not in member1.friends

def test_remove_friend():
    member2.remove_friend(member1)
    assert member1.username not in member2.friends
    assert member2.username not in member1.friends

def test_remove_friend_with_non_friend():
    assert member2.remove_friend(member1) == f"You're not friends with {member1.username}"

def test_build_inventory():
    assert inv1.username == 'peste'
    assert inv1.items == []

def test_add_item():
    inv1.add_item('dado', 'cubiliete')
    assert inv1.items == ['dado', 'cubiliete']

def test_remove_item():
    inv1.remove_item('dado')
    assert inv1.items == ['cubiliete']

def test_get_item():
    inv1.get_item('cubiliete') == 'cubiliete'

    

