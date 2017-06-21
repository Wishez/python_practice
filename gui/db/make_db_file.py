# -*- coding: utf-8 -*-
import shelve

dbfilename = 'people-file'
# ENDDB= 'enddb.'
# ENDREC = 'endrec.'
# RECSEC = '=>'
def storeDbase(db = False, data = False):

    # if data:
    #     filename = open(data['name'].split()[0].lower() + '.pkl', 'wb')
    #     # pickle.dump(data, filename)
    #     return

    tables = []

    for key in db:
        tables.append((key, db[key]))

    new_db = shelve.open('people-shelve')
    for (key, record)in tables:
        new_db[key] = record
    #     filename = open(key + '.pkl', 'wb')
    #     pickle.dump(record, filename)

    new_db.close()

def loadDbase(filename):
    # dbfile = open(filename, 'rb')
    db = shelve.open(filename)
    # data = pickle.load(dbfile)
    # dbfile.close()
    return db

if __name__ == '__main__':
    from gui.db.initdata import db
    storeDbase(db)


