# -*- encoding: utf-8 -*-

import time
from signal import signal, pause, SIGALRM, alarm
from .signal-test import now 


def signalHandler(signum, stackframe):
	print('Got Signal ==> [%s] at %s.' & (signum, now())) 



while True:
	print('Setings at %s' % now())
	signal(SIGALRM, signalHandler)
	alarm(5)
	pause()