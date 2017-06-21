# -*- coding: utf-8 -*-
import pprint

from manager import Manager

from gui.db.person import Person

# tables

people = []
# peopleValues = ['name', 'age', 'salary', 'job']
# bob = ['Bob Smith', 45, 40000, 'full-stack developer']
# sally = ['Sally Grinder', 42, 30000, 'front-end developer']
# tom = ['Tom Ridle', 50,  100000, 'Dark Lord']/
bob = Person('Bob Smith', 45, 40000, 'full-stack developer')
sally = Person('Sally Grinder', 42, 30000, 'front-end developer')
tom = Manager('Tom Ridle', 50,  100000, 'Dark Lord')
people.append(bob)
people.append(sally)
people.append(tom)
#db
db = {}
# for person in people:
    # db[person['name'].split()[0].lower()] = person

for person in people:
    db[person.firstName().lower()] = person

if __name__ == '__main__':
    bobData = db['bob']
    tomData = db['tom']
    bobData.addResponsibilities('Cleaner')
    bobData.increaceSalary(.20)
    tomData.increaceSalary(.10)
    pprint.pprint(bobData.getStatus())
    pprint.pprint(tomData.getStatus())
    print(bobData)
    print(tomData)
