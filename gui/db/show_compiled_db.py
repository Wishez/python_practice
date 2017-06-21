import pickle, glob, shelve

def showCompiledDb():
    db = shelve.open('people-shelve')
    # for filename in glob.glob('*.pkl'):
        # recfile = open(filename, 'rb')
        # record = pickle.load(recfile)
    for key in db:
        print(key, '=>\n', db[key])

showCompiledDb()