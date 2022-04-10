# class Person:


from collections import namedtuple
from operator import attrgetter


Person = namedtuple('Person', 'name, age')

p_1 = Person('Vasya', 25)
p_2 = Person('Kolya', 30)
p_3 = Person('Olya', 23)

people = [p_1, p_2, p_3]

print(people)

result = sorted(people)
print(result)


def by_age(person):
    return person.age


result = sorted(people, key=by_age)
print(result)

result2 = sorted(people, key=attrgetter('age'))
print(result2)
