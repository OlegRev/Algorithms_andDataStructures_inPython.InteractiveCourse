from collections import namedtuple


hero_1 = ('Aaz', 'Izverg', 100, 0.0, 250)
# File "task_6_namedtuple.py", line 5, in <module>    print(hero_1[5])
print(hero_1[4])


class Person:

    def __init__(self, name, race, health, mana, strength):
        self.name = name
        self.race = race
        self.health = health
        self.mana = mana
        self.strength = strength


hero_2 = Person('Aaz', 'Izverg', 100, 0.0, 250)
print(hero_2.mana)

New_Person = namedtuple('New_Person', 'name, race, health, mana, strength')
hero_3 = New_Person('Aaz', 'Izverg', 100, 0.0, 250)
print(hero_3.race)

prop = ['name', 'race', 'health', 'mana', 'strength']
New_Person_1 = namedtuple('New_Person_1', prop)
hero_4 = New_Person_1('Aaz', 'Izverg', 100, 0.0, 250)
print(hero_4.race)

prop_1 = ['name', '3race', 'health', '_mana', 'strength']
# New_Person_2 = namedtuple('New_Person_2', prop_1)
# ValueError: Type names and field names must be valid identifiers: '3race'
New_Person_2 = namedtuple('New_Person_2', prop_1, rename=True)
hero_5 = New_Person_2('Aaz', 'Izverg', 100, 0.0, 250)
print(hero_5)

print('*' * 50)
Point = namedtuple('Point', 'x, y, z')

p1 = Point(2, z=3, y=4)
print(p1)

t = [5, 10, 15]
p2 = Point._make(t)
print(p2)
# ._make(t: list) создание именовоного кортежа на основе списка

d2 = p2._asdict()
# ._asdict() позволяет преобразовать namedtuple -> OrderedDict
print(d2)

# p2.x = 6  # AttributeError: can't set attribute
p3 = p2._replace(x=6)
# ._replace(x:namedtuple.field)
# позволяет создавать новый объект
# с заменой поля оригинльного объекта namedtuple
print(p3)

print(p3._fields)
# Позволяет посмотреть какие поля есть у объекта namedtuple()

# работает с python ^3.7
print('*' * 50)
New_Ponit = namedtuple('New_Ponit', 'x, y, z', defaults=[0, 0])
p4 = New_Ponit(5)
print(p4)

print(p4._fields_defaults)
# ._fields_defaults позволяет получить словарь значений по умолчанию
# в виде словара key(поле): value(значение по умолчанию)

dct = {'x': 10, 'y': 20, 'z': 30}
p5 = New_Ponit(**dct)

# **dct: dict позволяет распаковать словарь в namedtuple()
