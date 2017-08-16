import os, sys

print('Child %s say %s.' % (os.getpid(), sys.argv[1]))

input('Wait for... what?')