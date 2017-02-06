import time
from functools import wraps


def time_spent_dec(func):
    @wraps(func)
    def dec(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        t1 = time.time()
        print "Spent time: {0}".format(t1 - t0)
        return result
    return dec
