keys  = ['name', 'age', 'salary', 'job']
bobValues = ['Bob Smith', 45, 40000, 'full-stack developer']
sallyValues = ['Sally Grinder', 42, 30000, 'front-end developer']

bob = dict(zip(keys, bobValues))
sally = dict(zip(keys, sallyValues))

people = [bob, sally]

namesPeople = list(map(lambda x: x['name'], people))


for person in people:
    personName = person['name']
    if type(personName) != 'dict':
        person['name'] = {
            'first': personName.split()[0],
            'last': personName.split()[1]
        }

db = {}
for person in people:
    tableName = person['name']['first'].lower()
    db[tableName] = person

#import pprint
#pprint.pprint(db)
print(db)