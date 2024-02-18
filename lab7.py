#Q1
class A:
    x, y = 0, 0
    def __init__(self):
        return
class B(A):
    def __init__(self):
        return
class C(A):
    def __init__(self):
        return
print(A.x, B.x, C.x)
#0 0 0
B.x = 2
print(A.x, B.x, C.x)
#0 2 0
A.x += 1
print(A.x, B.x, C.x)
#1 2 1
obj = C()
obj.y = 1
C.y = obj.y
A.y = obj.y
print(A.y, B.y, C.y, obj.y)
#1 1 1 1

#Q2
class Account:
    def __init__(self,holder,balance):
        self.holder = holder
        self.balance = balance
my_information = Account('john','10')
print(f"{my_information.holder} {my_information.balance}")

#Q4
class Card:
    cardtype = 'Staff'
    def __init__(self, name, attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense
        attack = 0
        defense = 0
staff_member = Card('staff', 400, 300)
print(f"{staff_member.name} {staff_member.attack} {staff_member.defense}")
other_staff = Card('other', 300, 500)
print(f"{other_staff.name} {other_staff.attack} {other_staff.defense}")