# -*- coding: utf-8 -*-
from gui.db.make_db_file import loadDbase

db = loadDbase('people-shelve')

for key in db:
    print('%s' % db[key])
    # for prop in db[key].__dict__:
    #     print('%s\t=>\t\n\t%s=>%s' % (key, prop, db[key]))

db.close()