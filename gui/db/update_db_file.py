from gui.db.make_db_file import loadDbase

db = loadDbase('people-shelve')

sally = db['sally']
sally['name'] = 'Sally Miller'
sally['salary'] *= 1.2
bob = db['bob']
bob['name'] = 'Bob Changed'
bob['salary'] = 2000
bob['job'] = 'undefined'
tom = db['tom']
tom['job'] += ', Destroyer'
tom['salary'] *= 1.5
db['sally'] = sally
db['bob'] = bob
db['tom'] = tom
db.close()
# storeDbase(data=sally)